import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


display_max_column = pd.set_option('display.max_columns', None)    # Show all columns
display_expand_frame = pd.set_option('display.expand_frame_repr', False)  # Prevent DataFrame from breaking into multiple lines
display_width = pd.set_option('display.width', 1000)  # Set the width large enough for DataFrame

##### ---- Gathering Data ---- #####
# 1. Gathering Data
# Load All Data
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
print(customers_df.head())
print()

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
print(orders_df.head())
print()

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
print(product_df.head())
print()

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
print(sales_df.head())
print()

# 2. Assessing Data
print(customers_df.info())
print()

## There is an anomaly number with sum of gender data,
## so it needs to be sum to know a number of missing values
## 1. Sum all of missing values
print(customers_df.isna().sum())
print()

## 2. Show all of summed duplicated data
print("Sum of duplicated data: ", customers_df.duplicated().sum())
print()

## 3. Summary of statistic parameter (mean, median, mode, etc.)
print(customers_df.describe())
print()

## 4. Assessing data orders_df
print(orders_df.info())
print()

## 5. Check duplicated data
print("Sum of duplicated data: ", orders_df.duplicated().sum())
print(orders_df.describe())
print()

## 6. Assessing data product_df
print(product_df.info())
print()

## 7. Check duplicated data
print("Sum of duplicated data: ", product_df.duplicated().sum())
print(product_df.describe())
print()

## 8. Assessing data sales_df
print(sales_df.info())
print()

## 9. Sum all of missing values
print(sales_df.isna().sum())
print()

## 10. Check duplicated data
print("Sum of duplicated data: ", sales_df.duplicated().sum())
print(sales_df.describe())
print()

# 3. Cleaning Data
## 1. Cleaning Data customer_df
### 1. Remove duplicate data
print(customers_df.drop_duplicates(inplace=True))
print()

### 2. Check duplicate data
print("Sum of duplicate data: ", customers_df.duplicated().sum())
print()

### 3. Handle missing values
### a. We need to filter the missing value
print(customers_df[customers_df.gender.isna()])
print()

### b. Then, we can use imputation method (replace with another value) to fix the missing values
### Imputation method chosen because the data frame has so much important information
### We can identify the dominant value, then fill the dominant value to gender column
print(customers_df.gender.value_counts())
print(customers_df.fillna(value="Prefer not to say", inplace=True))
print()

### c. Identify the missing value
print(customers_df.isna().sum())
print()

### d. Handle inaccurate value
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.max_rows', None)     # Show all rows (if necessary)
print(display_max_column)
print(display_expand_frame)
print(display_width)
print(customers_df[customers_df.age == customers_df.age.max()])
print()

### e. Replace false age by using replace method
print(customers_df.age.replace(customers_df.age.max(), 70, inplace=True))
print(customers_df.age.replace(customers_df.age.max(), 50, inplace=True))
print()

### f. Ensure the age equals to max age
print(customers_df[customers_df.age == customers_df.age.max()])
print()

### g. Ensure no inaccurate value
print(customers_df.describe())
print()

## 2. Cleaning Data orders_df
### Change wrong data type of order_date & delivery_date
datetime_columns = ["order_date", "delivery_date"]
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])

print(orders_df.info())
print()

## 3. Cleaning Data product_df
### Remove duplicate data
print(product_df.drop_duplicates(inplace=True))
print()
print("Sum of duplicate data: ", product_df.duplicated().sum())
print()

## 4. Cleaning Data sales_df
## Show data row that contains missing values
print(sales_df[sales_df.total_price.isna()])
print()

## 5. Calculate total price
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]
print(sales_df.isna().sum())
print()
##### ---- End of Gathering Data ---- #####

##### ---- Explanatory Data Analysis ---- #####
# 1. Exploration Data customers_df
## 1. Show all dataframe info
print(customers_df.describe(include="all"))
print()

## 2. Show customer demographics by gender
print(customers_df.groupby(by="gender").agg({
    "customer_id": "nunique",
    "age": ["max", "min", "mean", "std"]
}))
print()

## 3. Show customer demographics by city and state, sort by descending
print(customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False))
print()
print(customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False))
print()

##### ---- End of Explanatory Data Analysis ---- #####