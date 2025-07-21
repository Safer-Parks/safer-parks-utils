"""
Bounding Box Utilities for Geospatial Data Processing

This module provides utilities for filtering geospatial data within specified bounding boxes
and managing column selection for GeoDataFrames. It supports processing individual files
or batch processing multiple files using a CSV configuration.

Key Functions:
    - bounding_box_calc: Filter a single geospatial file by bounding box and columns
    - bounding_box_calc_table: Batch process multiple files using CSV configuration
    - cleaning: Filter GeoDataFrame columns to keep only specified columns
    - parse_bracket_list: Parse bracket-formatted lists from CSV strings

The module handles coordinate reference system (CRS) transformations and supports
filtering both spatial (bounding box) and attribute (column) dimensions of geospatial data.

Example:
    Process a single file:
    >>> bounding_box_calc(
    ...     input_file='data.geojson',
    ...     output_dir='output/',
    ...     bbox_coords=(-1.77, 53.79, -1.70, 53.82),
    ...     file_prefix='filtered',
    ...     clean=['column1', 'column2']
    ... )
    
    Batch process files:
    >>> bounding_box_calc_table('config.csv')
"""

import geopandas as gpd
import os
import re
from collections import defaultdict
from shapely.geometry import box
import pandas as pd

def parse_bracket_list(val):
    """
    Parse a bracket-formatted string containing column names into a list.
    
    Extracts content from strings like "['col1' 'col2' 'col3']" and returns
    a clean list of column names.
    
    Args:
        val (str): Bracket-formatted string containing column names
        
    Returns:
        list: List of parsed column names
    """
    # Extract content between brackets
    content = re.search(r'\[(.*?)\]', val).group(1)
    # Split by spaces but handle multi-word strings
    items = re.findall(r"'([^']*)'|\S+", content)
    # Flatten the results (regex returns tuples for groups)
    result = []
    for item in items:
        if isinstance(item, tuple):
            result.extend([x for x in item if x])
        elif item:
            result.append(item)
    return result

def bounding_box_calc(input_file, output_dir, bbox_coords, file_prefix, clean, crs=4326):
    """
    Filter a geospatial file by bounding box and selected columns.
    
    Loads a geospatial file, applies column filtering, handles CRS transformations,
    filters features within the specified bounding box, and saves the result.
    
    Args:
        input_file (str): Path to input geospatial file (GeoJSON, etc.)
        output_dir (str): Directory to save the filtered output
        bbox_coords (tuple): Bounding box coordinates (minx, miny, maxx, maxy)
        file_prefix (str): Prefix for the output filename
        clean (list): List of column names to keep in the output
        crs (int, optional): EPSG code for coordinate reference system. Defaults to 4326.
    """

    # Create output folder if it doesn't exist already
    os.makedirs(output_dir, exist_ok=True)

    # Load the GeoJSON file using GeoPandas
    gdf = gpd.read_file(input_file)

    # Apply column filtering
    gdf = cleaning(gdf, clean)

    # Then may have to do crs modification
    if crs=="no":
        pass
    elif crs==4326:
        pass
    else:
        # Trees is 27700
        gdf.set_crs(epsg=crs, inplace=True)
        gdf = gdf.to_crs(epsg=4326)

    # Create a bounding box geometry
    bbox = box(*bbox_coords)

    # Filter the GeoDataFrame to keep only points within the bounding box
    subset_gdf = gdf[gdf.geometry.within(bbox)]

    # Save the filtered data to a new GeoJSON file
    out_path = os.path.join(output_dir, f"{file_prefix}_subset.geojson")
    subset_gdf.to_file(out_path, driver="GeoJSON")

    # Print feedback so user is aware of progress
    print(f"Saved {len(subset_gdf)} features to {out_path}")

def bounding_box_calc_table(path_to_csv):
    """
    Batch process multiple geospatial files using CSV configuration.
    
    Reads a CSV file containing processing parameters for multiple files and
    applies bounding box filtering and column selection to each file specified.
    
    Args:
        path_to_csv (str): Path to CSV file with processing configuration.
                          Must contain columns: input_file, output_dir, minx, miny, 
                          maxx, maxy, file_prefix, crs, columns_to_keep
    """
    df = pd.read_csv(path_to_csv)
    print(df.columns)

    df["column_names"] = df['columns_to_keep'].apply(parse_bracket_list)
    
    # Iterate through each row and call bounding_box_calc
    for index, row in df.iterrows():
        # Extract the bounding box coordinates
        bbox_coords = (row['minx'], row['miny'], row['maxx'], row['maxy'])
        # Call the bounding_box_calc function with parameters from the row
        bounding_box_calc(
            input_file=str(row['input_file']),
            output_dir=str(row['output_dir']),
            bbox_coords=bbox_coords,
            file_prefix=str(row['file_prefix']),
            clean=row['column_names'],
            crs=row['crs']
        )

    print(f"Processed {len(df)} files from {path_to_csv}")

def cleaning(gdf, list_of_columns_to_keep):
    """
    Filter a GeoDataFrame to keep only specified columns.
    
    Args:
        gdf: GeoDataFrame to filter
        list_of_columns_to_keep: List of column names to keep
    
    Returns:
        Filtered GeoDataFrame with only the specified columns
    """
    if not list_of_columns_to_keep:
        return gdf
    
    print(f"Original columns: {list(gdf.columns)}")
    print(f"Columns to keep: {list_of_columns_to_keep}")
    
    # Ensure 'geometry' column is always included for GeoDataFrames
    columns_to_keep = list(list_of_columns_to_keep)
    filtered_gdf = gdf[columns_to_keep].copy()
    print(f"Final filtered columns: {list(filtered_gdf.columns)}")
    
    return filtered_gdf