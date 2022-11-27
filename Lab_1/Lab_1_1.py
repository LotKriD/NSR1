import pandas as pd
import os

years = {}
countries = {}

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'ufo_sighting_data.csv')
data = pd.read_csv(path)

for row in data:
    print(row)

for i in data['Date_time']:
    date = i.split(' ')[0]
    year = date.split('/')[2]
    count = 1

    for y in years.keys():
        if year == y:
            count = years[y] + 1

    years[year] = count

print("Years: ")
print(years)

for i in data['country']:
    count = 1

    for c in countries.keys():
        if i == c:
            count = countries[c] + 1

    countries[i] = count

print("Countries: ")
print(countries)
