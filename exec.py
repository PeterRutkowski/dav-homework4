import pandas as pd
import numpy as np

# import data
data = pd.read_csv('data/temperature.csv')

# delete day column
data = data.drop('day', axis=1)

# delete NaN values
delete_rows = []
for index, row in data.iterrows():
    delete_row = 0

    if type(row['City']) == float:
        if np.isnan(row['City']):
            delete_row = 1

    if type(row['country_id']) == float:
        if np.isnan(row['City']):
            delete_row = 1

    if type(row['Country']) == float:
        if np.isnan(row['City']):
            delete_row = 1

    if np.isnan(row['AverageTemperatureFahr']):
        delete_row = 1

    if np.isnan(row['AverageTemperatureUncertaintyFahr']):
        delete_row = 1

    if delete_row == 1:
        delete_rows.append(index)

data = data.drop(delete_rows)

data.to_csv('data/temperature_clean.csv', sep='\t', encoding='utf-8')

for col in data.columns:
    if col == 'AverageTemperatureFahr':
        col = 'AverageTemperatureCelsius'
    if col == 'AverageTemperatureUncertaintyFahr':
        col = 'AverageTemperatureUncertaintyCelsius'

for col in data.columns:
    print(col)

