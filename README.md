# Safer Parks Utils
Simple Python utility functions for processing geojson files for the Safer Parks open dashboard


## Development

To create a development environment, use the `environment.yml` file:

```bash
conda env create -f environment.yml
```

If you modify this file, you can update it easily:

```bash
conda env update --file environment.yml --prune
```

To use the environment:

```bash
conda activate safer_parks_utils-env
```
---

To run the tests, please activate the environment, and from the home directory run `pytest`
---

To use the Marimo notebooks: first, `cd` into the `development_notebooks` directory, and then run `marimo edit` (from inside the Conda environment). Note that these are for local development and treated as scratch; they will not run on your machine without example data saved under correct filenames.