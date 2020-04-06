from utils import import_data_4, plot_axes_4, save_plot
import pandas as pd
import numpy as np

def import_data_4a():
    data = pd.read_csv("data/temperatures_clean.csv")
    years = np.asarray(data['year'])
    countries = np.asarray(data['country_id'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])

    country_codes = ['BRA', 'FRA', 'JAP', 'NEW', 'POL', 'SOU', 'SWE', 'UKR']

    min_year = np.min(years)
    max_year = np.max(years)
    no_years = max_year-min_year+1

    final_years, final_averages = [], []

    for i in range(no_years):
        for j in range(len(country_codes)):
            temp_list = []
            for k in range(len(years)):
                if years[k] == i + min_year:
                    if countries[k] == country_codes[j]:
                        temp_list.append(average_temp_celsius[k])
            if len(temp_list) > 0:
                final_years.append(i+min_year)
                final_averages.append(np.average(temp_list))

    return final_years, final_averages

years, averages = import_data_4a()

fig, ax = plot_axes_4()

ax.plot(years, averages, color='black')

save_plot('4a')