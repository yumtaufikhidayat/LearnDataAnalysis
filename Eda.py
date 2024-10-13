import pandas as pd

city_names = ['Jakarta', 'Bandung', 'Makassar', 'Surabaya', 'Medan', 'Yogyakarta', 'Malang']
population = [498044, 964254, 491918, 8398748, 653115, 883305, 744955]
num_airports = [2, 2, 8, 3, 1, 3, 2]

df = pd.DataFrame({
    'City Name': city_names,
    'Population': population,
    'Airports': num_airports,
})

print(df.describe())
print()

# To show all complete parameters, we can use describe(include="all").
print(df.describe(include="all"))
print()

# To create a histogram, we can use hist()
print(df.hist())
print()

# To know the correlation among the numeric data, we can use corr() or cov()
print(df.cov())
print(df.corr())