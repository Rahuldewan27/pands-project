# analysis.py
# Author: Rahul Parvesh Dewan
# This program is created for the project of a module in ATU and will analyse and give outputs for the iris dataset.

# Importing the required libraries/modules that will help us in the analysis of the dataset and output the results.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Reading the dataset
    iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
                       names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

    while True:
        # Taking input from the user
        input_number = int(input("Enter the number against what you would like this program to do: \n1.Output a summary of each variable to a single text file(Enter 1) \n2.Save a histogram of each variable to png files(Enter 2) \n3.Output a scatter plot of each pair of variables(Enter 3) \n0.Exit \n"))

        # Drop duplicate rows as part of data cleaning
        iris.drop_duplicates(inplace=True)

        # Drop rows with missing values as part of data cleaning
        iris.dropna(inplace=True)

        # Function to output a summary of each variable to a single text file
        if input_number == 1: # If the user enters 1
            with open('summary.txt', 'w') as f: # Open a file named 'summary.txt' in write mode
                f.write(str(iris.describe())) # Write the summary of each variable to the file
            print("Summary of each variable has been saved to a single text file named 'summary.txt'.") # Print a message to the user
        # Function to save a histogram of each variable to png files
        elif input_number == 2: # If the user enters 2
            for column in iris.columns[:-1]: # Loop through each column in the dataset
                sns.histplot(data=iris, x=column) # Create a histogram of the column
                plt.title(f'Histogram of {column.capitalize()} (Species-wise)') # Set the title of the histogram
                plt.xlabel(f'{column.capitalize()}')    # Set the x-axis label of the histogram
                plt.ylabel('Frequency') # Set the y-axis label of the histogram
                plt.savefig(f'{column}_histogram.png') # Save the histogram to a png file
                plt.close() # Close the plot
            print("Histogram of each variable has been saved to png files.") # Print a message to the user
        # Function to output a scatter plot of each pair of variables
        elif input_number == 3: # If the user enters 3
            sns.pairplot(iris, hue='species', markers=["o", "s", "D"]) # Create a scatter plot of each pair of variables
            plt.savefig('scatter_plot.png') # Save the scatter plot to a png file
            print("Scatter plot of each pair of variables has been saved to a png file named 'scatter_plot.png'.") # Print a message to the user
        # Function to exit the program
        elif input_number == 0: # If the user enters 0
            print("Program has been exited.") # Print a message to the user
            break # Break the loop
        else: # If the user enters an invalid number
            print("Invalid number entered. Please enter a valid number.") # Print a message to the user

if __name__ == "__main__": # Call the main function
    main() 
