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
    import os
    cwd = os.getcwd()
    print(cwd)
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # input_file = "example_data/trees.geojson"
    input_file = "example_data/wy_crime.geojson"
    output_dir = "example_output"
    bbox_coords =  (-1.772833, 53.797893, -1.703482, 53.819777)
    # file_prefix = "peele_park" 
    file_prefix = "peel_park_crime" 
    return


@app.cell
def _():
    # spu.single_bb(input_file, output_dir, bbox_coords, file_prefix)
    return


@app.cell
def _(pd):
    # testing multiple batch imports


    df = pd.read_csv('data_to_process.csv')
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(spu):
    spu.multi_bb('data_to_process.csv')
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
