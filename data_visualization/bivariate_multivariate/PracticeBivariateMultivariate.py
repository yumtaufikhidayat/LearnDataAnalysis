import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Scatter Plot
## 1. Using scatter()
lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15,
                  9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93,
                132.93, 138.92, 145.98, 148.44, 152.81]

plt.scatter(x=lemon_diameter, y=lemon_weight)
print(plt.show())
print()

## 2. Using scatterplot()
sns.scatterplot(x=lemon_diameter, y=lemon_weight)
print(plt.show())
print()

## 3. Using regplot() to show correlation/relation among variables
sns.regplot(x=lemon_diameter, y=lemon_weight)
print(plt.show())
print()

# 2. Line Chart
## 1. Show line chart
plt.plot(lemon_diameter, lemon_weight)
print(plt.show())
print()

## 2. This codes below to show a realtime stock in BCA
url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
df = pd.read_csv(url, low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], color='red')
plt.xlabel('Date', size=15)
plt.ylabel('Price', size=15)
plt.show()
print(plt.show())
print()

# 3. Clustered Bar Chart
penguins = sns.load_dataset("penguins")
sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)
print(plt.show())
print()