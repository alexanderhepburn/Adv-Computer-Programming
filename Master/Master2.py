## Master 2: Basic of Pandas
## Description: Simple Pandas tasks
## Language: Python
## Author: Alexander Hepburn
## Date: 23.04.2024

# Import pandas
import pandas as pd

# read the table from github
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')

# Your tasks are below

# Task1
# See the first 25 entries

# Use the head function to print the first 25 entries
print(users.head(25))

# Task2
# See the last 10 entries

# Use the tail function to print the last 10 entries
print(users.tail(10))

# Task3
# What is the number of observations in the dataset?

# Use the shape function to print the number of observations
num_observations = users.shape[0]

print("Number of observations in the dataset:", num_observations)

# Task4
#What is the number of columns in the dataset?

# Use the shape function to print the number of columns
num_col = users.shape[1]

print("Number of columns in the dataset:", num_col)

# Task5
# What is the data type of each column?

# Use the dtypes value to print the data type of each column
column_types = users.dtypes

print("Data type of each column:")
print(column_types)

# Task 6
# How many different occupations there are in this dataset?

# Use the nunique function to print how many different occupations there are
num_unique_occupations = users['occupation'].nunique()

print("Number of different occupations in the dataset:", num_unique_occupations)

# Task 7
# Summarize the DataFrame.

# Use the describe with include all function to give a detailed description
summary = users.describe(include='all')

print("Summary of the df:")
print(summary)

# Task 8
# Summarize all the columns

# Use the describe without include all function to give a simple description of the columns
small_summary = users.describe()

print("Summary of the Columns:")
print(small_summary)


