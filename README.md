# Predicting Stress from Sleep and Lifestyle Factors

- by Yuheng Ouyang, Eduardo Rivera, Harpreet Singh, Songyang Yu
  Demo of a data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

## About

In this project we aim to develop a regression model that uses sleep-related, lifestyle, and physiological information to predict an individual’s self-reported stress level. Research shows that 30–40% of adults regularly sleep fewer than the recommended 7 hours**, and **more than one-third report high stress levels (CDC 2024; Sleep Foundation 2025). Our analysis examines how factors such as sleep duration, sleep quality, physical activity level, occupation, blood pressure category, BMI category, daily steps, and resting heart rate relate to perceived stress. Preliminary results show clear trends: individuals who report shorter or poorer-quality sleep, low activity levels, or elevated physiological indicators tend to experience higher stress. Our initial regression model performs reasonably well on unseen test data and captures meaningful associations; however, substantial variability remains, suggesting that stress is also influenced by unmeasured psychological or environmental factors. Although the model provides useful predictive insights, further refinement and additional features would likely be necessary for more precise stress estimation in real-world applications.

The dataset used in this project is the [*Sleep Health and Lifestyle Dataset*](https://www.kaggle.com/datasets/varishabatool/disorder) (Varishabatool n.d.), sourced from Kaggle. Each row represents one individual's self-reported information, including sleep duration, sleep quality, physical activity frequency, occupation type, BMI category, blood pressure category, resting heart rate, daily steps, and numeric stress level. Because the dataset combines behavioral, demographic, and physiological variables, it provides an opportunity to explore how multiple aspects of daily life relate to stress. These structured features also make the dataset suitable for regression modeling aimed at understanding and predicting stress levels.

## Developer Notes

### Developer dependencies
To run this project, the following tools and Python packages are required:

- [*Python*](https://www.python.org/)

- [*IPython*](https://ipython.readthedocs.io/)

- [*IPyKernel*](https://ipykernel.readthedocs.io/)

- [*Matplotlib*](https://matplotlib.org/)

- [*Pandas*](https://pandas.pydata.org/)

- [*Scikit-learn*](https://scikit-learn.org/)

- [*Altair*](https://altair-viz.github.io/)

- [*Pip*](https://pip.pypa.io/)

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
