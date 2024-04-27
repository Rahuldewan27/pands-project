# analysis.py
# Author: Rahul Parvesh Dewan
# This program is created for the project of a module in ATU and will analyse and give outputs for the iris dataset.

# Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the dataset
iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
                   names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Displaying the first 5 rows of the dataset
print(iris.head())

