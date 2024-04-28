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

# Taking input from the user
input_number = int(input("Enter the number against what you would like this program to do: \n1.Output a summary of each variable to a single text file(Enter 1) \n2.Save a histogram of each variable to png files(Enter 2) \n3.Output a scatter plot of each pair of variables(Enter 3) \n0.Exit \n"))

# Drop duplicate rows as part of data cleaning
iris.drop_duplicates(inplace=True)

# Drop rows with missing values as part of data cleaning
iris.dropna(inplace=True)

# Function to output a summary of each variable to a single text file
if input_number == 1:
    with open('summary.txt', 'w') as f:
        f.write(str(iris.describe()))
    print("Summary of each variable has been saved to a single text file named 'summary.txt'.")

# Function to save a histogram of each variable to png files
elif input_number == 2:
    for column in iris.columns[:-1]:
        sns.histplot(data=iris, x=column)
        plt.title(f'Histogram of {column.capitalize()} (Species-wise)')
        plt.xlabel(f'{column.capitalize()}')
        plt.ylabel('Frequency')
        plt.savefig(f'{column}_histogram.png')
        plt.close()
    print("Histogram of each variable has been saved to png files.")

# Function to output a scatter plot of each pair of variables
elif input_number == 3:
    sns.pairplot(iris, hue='species')
    plt.savefig('scatter_plot.png')
    print("Scatter plot of each pair of variables has been saved to a png file named 'scatter_plot.png'.")

# Function to exit the program
elif input_number == 0:
    print("Program has been exited.")

# If the user enters an invalid number and loop through the program till a valid number is entered by the user
if input_number != 1 and input_number != 2 and input_number != 3 and input_number != 0:
    while input_number != 1 and input_number != 2 and input_number != 3 and input_number != 0:
        print("Invalid number entered. Please enter a valid number.")
        input_number = int(input("Enter the number against what you would like this program to do: \n1.Output a summary of each variable to a single text file(Enter 1) \n2.Save a histogram of each variable to png files(Enter 2) \n3.Output a scatter plot of each pair of variables(Enter 3) \n0.Exit \n"))

# End of the program

