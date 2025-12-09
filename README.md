# Understanding Stress Through Sleep Patterns

- Yuheng Ouyang (@yhouyang02)
- Eduardo Rivera (@e-riveras)
- Harpreet Singh (@h4rrye)
- Songyang (Norton) Yu (@Spanorti08)

This repository contains our data analysis project for DSCI 522: Data Science Workflows.

## About

In this project we aim to develop a regression model that uses sleep-related, lifestyle, and physiological information to predict an individual’s self-reported stress level. Research shows that 30–40% of adults regularly sleep fewer than the recommended 7 hours, and more than one-third report high stress levels (CDC 2024[^cdc2024]; Sleep Foundation 2025[^sleep2025]). Our analysis explores whether shorter or poorer-quality sleeps are associated with higher stress, and we build regression models to assess how well these features can predict stress levels.

The dataset used in this project is the [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/varishabatool/disorder) (Varishabatool n.d.[^varisha]), sourced from Kaggle. We use a public image (Husn 2023[^husn2023]) to streamline the preprocessing. Each row represents one individual's self-reported information, including sleep duration, sleep quality, physical activity frequency, occupation type, BMI category, blood pressure category, resting heart rate, daily steps, and numeric stress level. Because the dataset combines behavioral, demographic, and physiological variables, it provides an opportunity to further explore how multiple aspects of daily life relate to stress. These structured features also make the dataset suitable for regression modeling aimed at understanding and predicting stress levels.

## How to run the data analysis

### In a Docker container (recommended)

Make sure you have [Docker](https://www.docker.com/get-started/) installed and running.

Pull the docker image from Docker Hub:

```bash
docker pull yhouyang02/dsci522-project-group01:latest
```

Run the docker container:

```bash
docker run --rm -it -p 8888:8888 yhouyang02/dsci522-project-group01:latest
```

Look in the terminal for a URL like:

```html
http://127.0.0.1:8888/lab?token=<some_long_token>
```

Open the URL in your web browser to launch Jupyter Lab.

Open a new Terminal in Jupyter Lab and run the following command to execute the analysis scripts. The scripts will download and preprocess the data, perform exploratory data analysis, and build the regression model.

```bash
python scripts/download_data.py
python scripts/clean_data.py
python scripts/eda.py 
python scripts/model.py
```

After the scripts finish running, run the following commands to generate the report in PDF and HTML format.

```bash
quarto render analysis/sleep-disorder-analysis.qmd --to pdf --output-dir docs
quarto render analysis/sleep-disorder-analysis.qmd --to html --output-dir docs
```

### In a local Conda environment

Clone the project repo and create the environment using `conda-lock` (recommended) or `conda`. Run one of the following commands from the root of this repository:

```bash
# conda-lock
conda-lock install --name dsci522 conda-lock.yml
```

```bash
# conda
conda env create -f environment.yml
```

Then activate the environment:

```bash
conda activate dsci522
```

Run the following command to execute the analysis scripts. The scripts will download and preprocess the data, perform exploratory data analysis, and build the regression model.

```bash
python scripts/download_data.py
python scripts/clean_data.py
python scripts/eda.py 
python scripts/model.py
```

Run the following commands to generate the report in PDF and HTML format.

```bash
quarto render analysis/sleep-disorder-analysis.qmd --to pdf --output-dir docs
quarto render analysis/sleep-disorder-analysis.qmd --to html --output-dir docs
```

### Interactively with Jupyter Notebook

If you follow either the Docker or Conda environment setup methods above, you will be able to read the results of our analysis in a report format without code snippets.

You can also run the analysis interactively in a Jupyter Notebook. After setting up the Conda environment as described above, launch Jupyter Lab and navigate to `analysis/sleep-disorder-analysis.ipynb`. Select an appropriate kernel (e.g., `dsci522` when run locally or `base` when run in a Docker container) and run the notebook cells to see the code and results.

## Dependencies

To run this project, the following tools and Python packages are required:

- [*Docker*](https://www.docker.com/) (version 29.0.1 or higher, if using Docker)

- [*Conda*](https://docs.conda.io/) (version 25.9.1 or higher)

- [*Conda-lock*](https://conda.github.io/conda-lock/) (version 3.0.4 or higher)

- [*Pip*](https://pip.pypa.io/) (version=25.2 or higher)

- [*Python*](https://www.python.org/) (version 3.12.11 or higher)

- [*IPython*](https://ipython.readthedocs.io/) (version 9.5.0 or higher)

- [*IPyKernel*](https://ipykernel.readthedocs.io/) (version 6.30.1 or higher)

- [*Pandas*](https://pandas.pydata.org/) (version 2.3.2 or higher)

- [*Scikit-learn*](https://scikit-learn.org/) (version=1.7.2 or higher)

- [*Altair*](https://altair-viz.github.io/) (version=6.0.0 or higher)

- [*Matplotlib*](https://matplotlib.org/) (version=3.10.6 or higher)

- [*Seaborn*](https://seaborn.pydata.org/) (version=0.13.2 or higher)

- [*SciencePlots*](https://github.com/garrettj403/SciencePlots) (version=2.2.0 or higher)

- [*Pandera*](https://pandera.readthedocs.io/) (version=0.20.4 or higher)

- [*Deepchecks*](https://docs.deepchecks.com/) (version 0.18.1 or higher)

- [*Click*](https://click.palletsprojects.com/) (version=8.2.1 or higher)

- [*Quarto*](https://quarto.org/) (version=1.3.313 or higher)

## License

The analysis code in this repository is released under the **MIT License**, permitting reuse, modification, and distribution with attribution.  
The documentation files (including this README) are released under the **Creative Commons CC0 1.0 Universal license**, allowing broad reuse with no restrictions.

For full legal details, please see the [LICENSE](./LICENSE.txt) file.

## References

[^cdc2024]: Centers for Disease Control and Prevention. (2024). *FastStats: Sleep in adults*. [https://www.cdc.gov/sleep/data-research/facts-stats/adults-sleep-facts-and-stats.html](https://www.cdc.gov/sleep/data-research/facts-stats/adults-sleep-facts-and-stats.html)

[^husn2023]: Husn, M. (2023). *Sleep health and lifestyle* [Data set]. GitHub. [https://raw.githubusercontent.com/Muhanad-husn/Sleep-Health-and-Lifestyle/main/data.csv](https://raw.githubusercontent.com/Muhanad-husn/Sleep-Health-and-Lifestyle/main/data.csv)

[^sleep2025]: Sleep Foundation. (2025). *100+ sleep statistics – Facts and data about sleep 2024*. [https://www.sleepfoundation.org/how-sleep-works/sleep-facts-statistics](https://www.sleepfoundation.org/how-sleep-works/sleep-facts-statistics)

[^varisha]: Varishabatool. (n.d.). *Sleep health and lifestyle dataset* [Data set]. Kaggle. [https://www.kaggle.com/datasets/varishabatool/disorder](https://www.kaggle.com/datasets/varishabatool/disorder)
