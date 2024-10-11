import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


display_max_column = pd.set_option('display.max_columns', None)    # Show all columns
display_expand_frame = pd.set_option('display.expand_frame_repr', False)  # Prevent DataFrame from breaking into multiple lines
display_width = pd.set_option('display.width', 1000)  # Set the width large enough for DataFrame

# 1. Gathering Data
# Load All Data
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
# print(customers_df.head())
# print("\n")

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
# print(orders_df.head())
# print("\n")

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
# print(product_df.head())
# print("\n")

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
# print(sales_df.head())
# print("\n")

# 2. Assessing Data
# print(customers_df.info())
# print("\n")

## There is an anomaly number with sum of gender data,
## so it needs to be sum to know a number of missing values
## 1. Sum all of missing values
# print(customers_df.isna().sum())
# print("\n")

## 2. Show all of summed duplicated data
# print("Sum of duplicated data: ", customers_df.duplicated().sum())
# print("\n")

## 3. Summary of statistic parameter (mean, median, mode, etc.)
# print(customers_df.describe())
# print("\n")

## 4. Assessing data orders_df
# print(orders_df.info())
# print("\n")

## 5. Check duplicated data
# print("Sum of duplicated data: ", orders_df.duplicated().sum())
# print(orders_df.describe())
# print("\n")

## 6. Assessing data product_df
# print(product_df.info())
# print("\n")

## 7. Check duplicated data
# print("Sum of duplicated data: ", product_df.duplicated().sum())
# print(product_df.describe())
# print("\n")

## 8. Assessing data sales_df
# print(sales_df.info())
# print("\n")

## 9. Sum all of missing values
# print(sales_df.isna().sum())
# print("\n")

## 10. Check duplicated data
# print("Sum of duplicated data: ", sales_df.duplicated().sum())
# print(sales_df.describe())
# print("\n")

# 3. Cleaning Data
## 1. Cleaning Data customer_df
### 1. Remove duplicate data
# print(customers_df.drop_duplicates(inplace=True))
# print("\n")

### 2. Check duplicate data
# print("Sum of duplicate data: ", customers_df.duplicated().sum())
# print("\n")

### 3. Handle missing values
### a. We need to filter the missing value
# print(customers_df[customers_df.gender.isna()])
# print("\n")

### b. Then, we can use imputation method (replace with another value) to fix the missing values
### Imputation method chosen because the data frame has so much important information
### We can identify the dominant value, then fill the dominant value to gender column
# print(customers_df.gender.value_counts())
# print(customers_df.fillna(value="Prefer not to say", inplace=True))
# print("\n")

### c. Identify the missing value
# print(customers_df.isna().sum())
# print("\n")

### d. Handle inaccurate value
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.max_rows', None)     # Show all rows (if necessary)
# print(display_max_column)
# print(display_expand_frame)
# print(display_width)
# print(customers_df[customers_df.age == customers_df.age.max()])
# print("\n")

### e. Replace false age by using replace method
# print(customers_df.age.replace(customers_df.age.max(), 70, inplace=True))
# print(customers_df.age.replace(customers_df.age.max(), 50, inplace=True))
# print("\n")

### f. Ensure the age equals to max age
# print(customers_df[customers_df.age == customers_df.age.max()])
# print("\n")

### g. Ensure no inaccurate value
# print(customers_df.describe())
# print("\n")