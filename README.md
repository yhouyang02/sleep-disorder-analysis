# Understanding Stress Through Sleep Patterns

- Yuheng Ouyang  
- Eduardo Rivera  
- Harpreet Singh  
- Songyang (Norton) Yu  

This repository contains our data analysis project for DSCI 522 (Data Science Workflows).

## About

In this project we aim to develop a regression model that uses sleep-related, lifestyle, and physiological information to predict an individual’s self-reported stress level. Research shows that 30–40% of adults regularly sleep fewer than the recommended 7 hours, and more than one-third report high stress levels (CDC 2024; Sleep Foundation 2025). Our analysis explores whether shorter or poorer-quality sleeps are associated with higher stress, and we build regression models to assess how well these features can predict stress levels.

The dataset used in this project is the [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/varishabatool/disorder) (Varishabatool n.d.), sourced from Kaggle. Each row represents one individual's self-reported information, including sleep duration, sleep quality, physical activity frequency, occupation type, BMI category, blood pressure category, resting heart rate, daily steps, and numeric stress level. Because the dataset combines behavioral, demographic, and physiological variables, it provides an opportunity to further explore how multiple aspects of daily life relate to stress. These structured features also make the dataset suitable for regression modeling aimed at understanding and predicting stress levels.

## How to run the data analysis
First time running the project, create the environment using `conda-lock` (preferred) or `conda`. Run one of the following commands from the root of this repository:
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

To launch the analysis, run:
```bash
jupyter lab
```

Then open the notebook:
Open `sleep-disorder-analysis.ipynb` in Jupyter Lab, go to Kernel, then Select Kernel, and choose Python `[conda env:dsci522]`.


## Dependencies
To run this project, the following tools and Python packages are required:

- [*Conda*](https://docs.conda.io/) (version 25.9.1 or higher)

- [*Conda-lock*](https://conda.github.io/conda-lock/) (version 3.0.4 or higher)

- [*Python*](https://www.python.org/) (version 3.12.11 or higher)

- [*IPython*](https://ipython.readthedocs.io/) (version 9.5.0 or higher)

- [*IPyKernel*](https://ipykernel.readthedocs.io/) (version 6.30.1 or higher)

- [*Pandas*](https://pandas.pydata.org/) (version 2.3.2 or higher)

- [*Scikit-learn*](https://scikit-learn.org/) (version=1.7.2 or higher)

- [*Altair*](https://altair-viz.github.io/) (version=6.0.0 or higher)

- [*Matplotlib*](https://matplotlib.org/) (version=3.10.6 or higher)

- [*Seaborn*](https://seaborn.pydata.org/) (version=0.13.2 or higher)

- [*SciencePlots*](https://github.com/garrettj403/SciencePlots) (version=2.2.0 or higher)

- [*Pip*](https://pip.pypa.io/) (version=25.2 or higher)


## License

The analysis code in this repository is released under the **MIT License**, permitting reuse, modification, and distribution with attribution.  
The documentation files (including this README) are released under the **Creative Commons CC0 1.0 Universal license**, allowing broad reuse with no restrictions.

For full legal details, please see the [LICENSE](./LICENSE.txt) file.



## References

Centers for Disease Control and Prevention. (2024). *FastStats: Sleep in adults*. https://www.cdc.gov/sleep/data-research/facts-stats/adults-sleep-facts-and-stats.html

Husn, M. (2023). *Sleep health and lifestyle* [Data set]. GitHub. https://raw.githubusercontent.com/Muhanad-husn/Sleep-Health-and-Lifestyle/main/data.csv

Sleep Foundation. (2025). 100+ sleep statistics – Facts and data about sleep 2024. https://www.sleepfoundation.org/how-sleep-works/sleep-facts-statistics

Varishabatool. (n.d.). *Sleep health and lifestyle dataset* [Data set]. Kaggle. https://www.kaggle.com/datasets/varishabatool/disorder

