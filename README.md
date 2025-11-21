# Predicting Stress from Sleep and Lifestyle Factors

- Yuheng Ouyang  
- Eduardo Rivera  
- Harpreet Singh  
- Songyang (Norton) Yu  

This repository contains our data analysis project for DSCI 522 (Data Science Workflows)

## About

In this project we aim to develop a regression model that uses sleep-related, lifestyle, and physiological information to predict an individual’s self-reported stress level. Research shows that 30–40% of adults regularly sleep fewer than the recommended 7 hours**, and **more than one-third report high stress levels (CDC 2024; Sleep Foundation 2025). Our analysis examines how factors such as sleep duration, sleep quality, physical activity level, occupation, blood pressure category, BMI category, daily steps, and resting heart rate relate to perceived stress. Preliminary results show clear trends: individuals who report shorter or poorer-quality sleep, low activity levels, or elevated physiological indicators tend to experience higher stress. Our initial regression model performs reasonably well on unseen test data and captures meaningful associations; however, substantial variability remains, suggesting that stress is also influenced by unmeasured psychological or environmental factors. Although the model provides useful predictive insights, further refinement and additional features would likely be necessary for more precise stress estimation in real-world applications.

The dataset used in this project is the [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/varishabatool/disorder) (Varishabatool n.d.), sourced from Kaggle. Each row represents one individual's self-reported information, including sleep duration, sleep quality, physical activity frequency, occupation type, BMI category, blood pressure category, resting heart rate, daily steps, and numeric stress level. Because the dataset combines behavioral, demographic, and physiological variables, it provides an opportunity to explore how multiple aspects of daily life relate to stress. These structured features also make the dataset suitable for regression modeling aimed at understanding and predicting stress levels.

## How to run the data analysis
First time running the project, run the following from the root of this repository:
```bash
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
Open `sleep-disorder-analysis.ipynb` in Jupyter Lab and select the correct kernel.


## Dependencies
To run this project, the following tools and Python packages are required:

- [*Python*](https://www.python.org/) (version=3.12.11 or higher)

- [*IPython*](https://ipython.readthedocs.io/) (version=9.5.0 or higher)

- [*IPyKernel*](https://ipykernel.readthedocs.io/) (version=6.30.1 or higher)

- [*Matplotlib*](https://matplotlib.org/) (version=3.10.6 or higher)

- [*Pandas*](https://pandas.pydata.org/) (version=2.3.2 or higher)

- [*Scikit-learn*](https://scikit-learn.org/) (version=1.7.2 or higher)

- [*Altair*](https://altair-viz.github.io/) (version=6.0.0 or higher)

- [*Pip*](https://pip.pypa.io/) (version=25.2 or higher)

- [*Conda*](https://docs.conda.io/)

## License

The analysis code in this repository is released under the **MIT License**, permitting reuse, modification, and distribution with attribution.  
The documentation files (including this README) are released under the **Creative Commons CC0 1.0 Universal license**, allowing broad reuse with no restrictions.

For full legal details, please see the [LICENSE](./LICENSE.txt) file.



## References

Varishabatool. n.d. “Sleep Health and Lifestyle Dataset.” Kaggle.  
https://www.kaggle.com/datasets/varishabatool/disorder.

Centers for Disease Control and Prevention (CDC). 2024. “FastStats: Sleep in Adults.”  
National Center for Health Statistics.  
https://www.cdc.gov/sleep/data-research/facts-stats/adults-sleep-facts-and-stats.html.

Sleep Foundation. 2025. “Sleep Statistics: Updated 2024–2025.”  
National Sleep Foundation.  
https://www.sleepfoundation.org/how-sleep-works/sleep-facts-statistics.
