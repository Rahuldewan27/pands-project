### Iris Dataset Summary

## Origin and purpose of the dataset

British statistician and biologist Ronald Fisher in 1936 developed this data set. The development was done to demonstrate analysis based on classification into predifined categories.
His goal was to show that multiple measurements could be used to differentiate between flower specicies.

The data set itself was desgined to show statistical analysis, specially around discriminant analysis.

## Describing the contents of the dataset

1. Species - The species of the flower. This is categorical data type
2. Sepal Length - Sepal helps protects the flower and is the outer part of the flower. This variable takes the sepal length in centimeters. It is of floating data type.
3. Sepeal Width -Sepal helps protects the flower and is the outer part of the flower. This variable takes the sepal width in centimeters. It is of floating data type.
4. Petal Length - Petal is the colorful innerpart of the flower. This variable takes the petal length in centimeters. It is of floating data type.
5. Petal Width  - Petal is the colorful innerpart of the flower. This variable takes the petal lwidth in centimeters. It is of floating data type.


## Relevant background information

- The data set itself was collected by Edgar Andreson.
- The data set has a limitation in its size, the sample size is relatively small and hence may contain biasness towards something.
- The data set is freely available on multiple platforms including python website and uci machine learning repositorty

## Approach taken
- First imported all neccessary modules for the program
- Then data set was loaded and cleaned with an attempt to drop duplicates and remove na values
- Once data clean up was done, I have procceeded to define the base of the loops i.e what do I want the program to deliver as outputs(Summary of data, histograms, corelations) 
- On defining the basics output deliverable I then procceeded to keep refining how I wanted the loop to behave in commander(I used extensive testing for this)
- Once the program was defined I kept iterating on cleaning up on how I wanted the histogram and corelation outputs to look
- Comments were added as appropriate

## Referances

1. "Iris flower data set." Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 26 November 2023. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
3. Fisher, R. A. "The Use of Multiple Measurements in Taxonomic Problems." Annals of Eugenics 7.2 (1936): 179-188. https://doi.org/10.1111/j.1469-1809.1936.tb02137.x
4. w3schools. (n.d.). Python NumPy. https://www.w3schools.com/python/numpy/default.asp -This is to import and understand the Numpy module
5. w3schools. (n.d.). Python Pandas. https://www.w3schools.com/python/pandas/default.asp =This is to import and understand the pandas module
6. w3schools. (n.d.). Python Pandas DataFrames. https://www.w3schools.com/python/pandas/pandas_dataframes.asp =This is to import and understand how to deal with data frames and understand the clean up process
7. w3schools. (n.d.). Python NumPy Random and Seaborn. https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp =This is to import and understand statistical calculations in the data set
8. Real Python. (n.d.). Pandas DataFrame 101. https://realpython.com/courses/pandas-dataframes-101/ =This was used further further to understand cleaning up the data set for visualisation
9. Real Python. (n.d.). Pandas: Python Explore Dataset. https://realpython.com/pandas-python-explore-dataset/ -Used for viewing lines and understanding attributes/charachteristics of the data set
10. Real Python. (n.d.). Python Histograms. https://realpython.com/python-histograms/ -Understanding visualisations of the histograms
11. Real Python. (n.d.). Python Bar Charts with Matplotlib. https://realpython.com/python-bar-charts-matplotlib/ -Understand visualsaition of the bar charts
12. Pandas. (n.d.). DataFrame.corr. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html -Understanding and plotting corelations for the variables in the data set
13. Real Python. (n.d.). Exploring Correlation in Python. https://realpython.com/numpy-scipy-pandas-correlation-python/ -Further understanding the corelation of the data set


