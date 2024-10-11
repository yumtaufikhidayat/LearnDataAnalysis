import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# 1. Gathering Data
# Load All Data
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
# print(customers_df.head())

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
# print(orders_df.head())

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
# print(product_df.head())

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
# print(sales_df.head())

# 2. Assessing Data
# print(customers_df.info())

## There is an anomaly number with sum of gender data,
## so it needs to be sum to know a number of missing values
## 1. Sum all of missing values
# print(customers_df.isna().sum())

## 2. Show all of summed duplicated data
# print("Sum of duplicated data: ", customers_df.duplicated().sum())

## 3. Summary of statistic parameter (mean, median, mode, etc.)
# print(customers_df.describe())

## 4. Assessing data orders_df
# print(orders_df.info())

## 5. Check duplicated data
# print("Sum of duplicated data: ", orders_df.duplicated().sum())
# print(orders_df.describe())

## 6. Assessing data product_df
# print(product_df.info())

## 7. Check duplicated data
# print("Sum of duplicated data: ", product_df.duplicated().sum())
# print(product_df.describe())

## 8. Assessing data sales_df
# print(sales_df.info())

## 9. Sum all of missing values
# print(sales_df.isna().sum())

## 10. Check duplicated data
print("Sum of duplicated data: ", sales_df.duplicated().sum())
print(sales_df.describe())