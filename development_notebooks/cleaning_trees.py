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
    input_file = "example_data/trees.geojson"
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
def _(gdf):
    gdf.head()
    return


@app.cell
def _():
    columns_to_keep = ['geometry']
    return (columns_to_keep,)


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
