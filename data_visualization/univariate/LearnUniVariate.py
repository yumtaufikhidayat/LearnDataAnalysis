import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta',
          'Surakarta', 'Surabaya', 'Medan', 'Makassar')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)

# 1. Bar Chart
## 1. Show bar chart by using matplotlib
plt.bar(x=cities, height=populations)
print(plt.show())

### Use xticks() and adjust rotation parameter to setting up category value on X axis
plt.bar(x=cities, height=populations)
plt.xticks(rotation=45)
print(plt.show())

### Use barh() to show bar diagram in horizontal
### If using barh() make sure to input the Y axis and width
plt.barh(y=cities, width=populations)
print(plt.show())

## 2. Show bar chart using pandas
### Sort by highest population
df = pd.DataFrame({
    'Cities': cities,
    'Population': populations,
})

df.sort_values(by='Population', inplace=True)
plt.barh(y=df["Cities"], width=df["Population"])
print(plt.show())

### Show labels
plt.barh(y=df["Cities"], width=df["Population"])
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
print(plt.show())

## 3. Show bar chart using seaborn
### Show bar chart using seaborn
sns.barplot(y=df["Cities"], x=df["Population"], orient="h", color='blue')
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
print(plt.show())

# 2. Pie Chart
## 1. Show bar chart using matplotlib
flavors = ('Chocolate', 'Vanilla', 'Macha', 'Others')
votes = (50, 20, 30, 10)
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.1, 0, 0, 0)

plt.pie(
    x=votes,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)
print(plt.show())

### Use wedgedrops() to show a hole in center like a donut
plt.pie(
    x=votes,
    labels=flavors,
    colors=colors,
    wedgeprops = {'width': 0.4}
)
print(plt.show())

# 3. Histogram
## 1. Show histogram using numpy
### Show random data but as normal distribution
x = np.random.normal(15, 5, 250)
plt.hist(x=x, bins=15)
print(plt.show())

## 2. Show histogram using seaborn
### Use histplot() to show readable histogram
sns.histplot(x=x, bins=15)
print(plt.show())

### Identify the distribution from qualitative data
sns.histplot(x=x, bins=15, kde=True)
print(plt.show())

# 4. Box Plot
x = np.random.normal(15, 5, 250)
sns.boxplot(x)
plt.show()