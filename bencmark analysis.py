#imorting all the libraries that are required
import pandas as pd
import numpy as np
import csv
import matplotlib as mt
import matplotlib.pyplot as plt
import seaborn as sns

#bringing CSV file or the dataset into python to analyze
read=pd.read_csv("D:/python projects/archive/GSMArena_Benchmarks.csv")
print(read.head())
print(read.isnull())

#filling all the empty values by NA
print(read.fillna("NA"))

#finding the average
mean=read.mean(axis=1,numeric_only=True)
print(mean)
#creating two sorted datasets 
d=read.sort_values(by=["BasemarkOS"])
d2=read.sort_values(by=["BasemarkX"])

#describing the dataset by which it will return mean,count,etc.
print(read.describe())

#creating graph for the first sorted data
plt.subplot(2,1,1)
sns.scatterplot(data=d.tail(10), x="BasemarkOS", y="Phone" , hue='Phone')

#creating graph for the secoond sorted data
plt.subplot(2,1,2)
plot1=sns.barplot(data=d2.head(10), x="BasemarkX", y="Phone")

#displaying the graph
plt.show()
