import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sys import argv

def import_data_2():
    data = pd.read_csv("data/temperatures_clean.csv")
    years = np.asarray(data['year'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
    return years, average_temp_celsius

def import_data_3():
    data = pd.read_csv("data/temperatures_clean.csv")
    countries = np.asarray(data['country_id'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])

    country_codes = ['BRA', 'FRA', 'JAP', 'NEW', 'POL', 'SOU', 'SWE', 'UKR']

    temp_indices = []
    for i in range(len(country_codes)):
        temp_indices.append([])
    for i in range(len(countries)):
        for j in range(len(country_codes)):
            if countries[i] == country_codes[j]:
                temp_indices[j].append(i)

    average_temp_celsius_split = []
    for i in range(len(temp_indices)):
        temp_single_country = []
        for j in range(len(temp_indices[i])):
            temp_single_country.append(average_temp_celsius[temp_indices[i][j]])
        average_temp_celsius_split.append(temp_single_country)

    return country_codes, average_temp_celsius_split

def plot_axes_2():
    fig, ax = plt.subplots()

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_ylim(-18, 32)
    ax.set_xlim(1730, 2025)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    major_x_ticks = np.arange(1800, 2025, 100)
    minor_x_ticks = np.arange(1750, 2025, 50)
    major_y_ticks = np.arange(-10, 32, 10)
    minor_y_ticks = np.arange(-15, 32, 5)

    ax.set_xticks(major_x_ticks)
    ax.set_xticks(minor_x_ticks, minor=True)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')

    plt.ylabel('AverageTemperatureCelsius')
    plt.xlabel('year')
    plt.tight_layout()
    plt.grid(True, zorder=0, color='white')
    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.4)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=1)

    return fig, ax

def plot_axes_3():
    fig, ax = plt.subplots()

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(-18, 32)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    major_y_ticks = np.arange(-10, 32, 10)
    minor_y_ticks = np.arange(-15, 32, 5)

    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    ax.tick_params(axis='y', colors='grey', which='minor')

    plt.ylabel('AverageTemperatureCelsius')
    plt.xlabel('country_id')
    plt.tight_layout()
    plt.grid(True, zorder=0, color='white')
    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.4)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=1)
    ax.set_axisbelow(True)

    return fig, ax

def plot_axes_4():
    fig, ax = plt.subplots()

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_ylim(-5, 22)
    ax.set_xlim(1730, 2025)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    major_x_ticks = np.arange(1800, 2025, 100)
    minor_x_ticks = np.arange(1750, 2025, 50)
    major_y_ticks = np.arange(0, 22, 5)
    minor_y_ticks = np.arange(-5, 22, 2.5)

    ax.set_xticks(major_x_ticks)
    ax.set_xticks(minor_x_ticks, minor=True)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')

    plt.ylabel('AverageTemperatureCelsius')
    plt.xlabel('year')
    plt.tight_layout()
    plt.grid(True, zorder=0, color='white')
    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.4)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=1)

    return fig, ax

def import_data_4a():
    data = pd.read_csv("data/temperatures_clean.csv")
    years = np.asarray(data['year'])
    countries = np.asarray(data['country_id'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])

    country_codes = ['BRA', 'FRA', 'JAP', 'NEW', 'POL', 'SOU', 'SWE', 'UKR']

    min_year = np.min(years)
    max_year = np.max(years)
    no_years = max_year - min_year + 1

    country_split, averages_split = [], []
    # create template for plugging in averages
    for i in range(len(country_codes)):
        country_split.append([])
        averages_split.append([])
        for j in range(no_years):
            country_split[i].append([])
            averages_split[i].append([])
    # plug in avarages to the template
    for i in range(len(countries)):
        for j in range(len(country_codes)):
            if countries[i] == country_codes[j]:
                country_split[j][years[i]-min_year].append(average_temp_celsius[i])
    # calculate avarages of plugged in data in the template
    for i in range(len(country_split)):
        for j in range(len(country_split[i])):
            if len(country_split[i][j]) > 0:
                averages_split[i][j] = np.average(country_split[i][j])
            else:
                averages_split[i][j] = 100
    # list of all years between min_year and max_year
    possible_years = np.arange(min_year, max_year+1,1)
    # lists for storing final results
    final_years, final_averages = [], []

    for i in range(len(averages_split)):
        clean_years, clean_averages = [], []
        for j in range(len(averages_split[i])):
            if averages_split[i][j] != 100:
                clean_years.append(possible_years[j])
                clean_averages.append(averages_split[i][j])
        final_years.append(clean_years)
        final_averages.append(clean_averages)

    print(np.shape(final_years), np.shape(final_averages))

    return final_years, final_averages

def save_plot(filename):
    if len(argv) > 1:
        if argv[1] == '0':
            plt.show()
        else:
            plt.savefig('plots/' + filename + '.png', dpi=200)
    else:
        plt.savefig('plots/' + filename + '.png', dpi=200)