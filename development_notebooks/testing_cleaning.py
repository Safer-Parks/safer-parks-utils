import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import safer_parks_utils as spu

    import importlib
    importlib.reload(spu)
    return (spu,)


@app.cell
def _():
    import geopandas as gpd
    import os
    import re
    from collections import defaultdict
    from shapely.geometry import box
    import pandas as pd
    return gpd, pd


@app.cell
def _(pd):
    df = pd.read_csv('data_to_process_v2.csv')
    return (df,)


@app.cell
def _(df, spu):
    df["column_names"] = df['columns_to_keep'].apply(spu.bounding_box.parse_bracket_list)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, gpd):
    gdf = gpd.read_file(df.input_file[0])
    return (gdf,)


@app.cell
def _(gdf):
    gdf.head()
    return


@app.cell
def _(df):
    bbox_coords = (df['minx'][0], df['miny'][0], df['maxx'][0], df['maxy'][0])
    return (bbox_coords,)


@app.cell
def _(bbox_coords, df, spu):
    spu.bounding_box.bounding_box_calc(
        df.input_file[0],
        df.output_dir[0],
        bbox_coords,
        df.file_prefix[0],
        df.column_names[0],
        crs=df.crs[0]
    )
    return


@app.cell
def _(df):
    df.column_names[0]
    return


@app.cell
def _():
    type(None)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
