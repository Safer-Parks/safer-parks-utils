import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import safer_parks_utils as spu

    import importlib
    importlib.reload(spu)
    return


@app.cell
def _():
    import geopandas as gpd
    import os
    import re
    from collections import defaultdict
    from shapely.geometry import box
    import pandas as pd
    return (gpd,)


@app.cell
def _():
    input_file = "example_data/wy_crime.geojson"
    return (input_file,)


@app.cell
def _(gpd, input_file):
    gdf = gpd.read_file(input_file)
    return (gdf,)


@app.cell
def _(gdf):
    gdf.columns
    return


@app.cell
def _(c):
    c
    return


@app.cell
def _():
    columns_to_keep = ['Longitude',
           'Latitude', 'Location', 'Crime type']
    return (columns_to_keep,)


@app.cell
def _():
    # On or near Park/Open Space
    return


@app.cell
def _(gdf):
    (gdf['Location'] == 'On or near Park/Open Space').sum()
    return


@app.cell
def _(gdf):
    # Contains the text (partial match)
    count = gdf['Location'].str.contains('Park/Open Space', na=False).sum()
    return (count,)


@app.cell
def _(count):
    count
    return


@app.cell
def _(gdf):
    # See unique values in the Crime type column
    print(gdf['Crime type'].unique())

    # Or see value counts
    print(gdf['Crime type'].value_counts())

    # Check for the specific value
    print('On or near Park/Open Space' in gdf['Location'].values)
    return


@app.cell
def _(columns_to_keep, gdf):
    new_df = gdf[columns_to_keep]
    return (new_df,)


@app.cell
def _(new_df):
    new_df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
