"""
Attempt at answering initial EDA questions on the Grocery dataset
"""
import pandas as pd

#Load in csvs as dataframes
data = pd.read_csv('sales_data_2017_2018.csv')
print(data.dtypes)
#print(data.head())

#Get percent of dataset with null values for each column for restaurants data:
for columnName in data.columns.values:
    null_list = data[columnName].isnull()
    COUNTNULL = 0
    COUNTNOTNULL = 0
    for isratingnull in null_list:
        if isratingnull is True:
            COUNTNULL += 1
        else:
            COUNTNOTNULL += 1
    print("For", columnName, COUNTNULL, "/", COUNTNULL+COUNTNOTNULL,
          COUNTNULL/(COUNTNULL+COUNTNOTNULL))
