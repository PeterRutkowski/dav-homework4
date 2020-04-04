import pandas as pd
import numpy as np
from scipy.constants import convert_temperature

# import data
data = pd.read_csv('data/temperature.csv')

# delete day column
data = data.drop('day', axis=1)

# delete NaN values
dropped_rows = []
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
        dropped_rows.append(index)

data = data.drop(dropped_rows)

# rename Fahrenheit do Celsius
data = data.rename(columns={'AverageTemperatureFahr': 'AverageTemperatureCelsius',
                            'AverageTemperatureUncertaintyFahr': 'AverageTemperatureUncertaintyCelsius'})

# convert Fahrenheit do Celsius
for index, row in data.iterrows():
    data['AverageTemperatureCelsius'][index] = \
        np.round(convert_temperature(data['AverageTemperatureCelsius'][index], 'F', 'C'), 4)
    data['AverageTemperatureUncertaintyCelsius'][index] = \
        np.round(convert_temperature(data['AverageTemperatureUncertaintyCelsius'][index], 'F', 'C'), 3)

# save cleaned dataframe to a csv file
data.to_csv('data/temperature_clean.csv', sep=',', encoding='utf-8')