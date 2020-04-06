import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def import_AvTempCelsius():
    data = pd.read_csv("data/temperatures_clean.csv")
    years = np.asarray(data['year'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
    return years, average_temp_celsius

def plot_background(x_low, x_up, y_low, y_up):
    fig, ax = plt.subplots()

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_ylim(y_low, y_up)
    ax.set_xlim(x_low, x_up)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    x_lower_bound_major = x_low
    x_lower_bound_minor = x_low
    for i in range(100):
        if (x_lower_bound_major + i)%100 == 0:
            x_lower_bound_major = x_lower_bound_major + i
            break
    for i in range(50):
        if (x_lower_bound_minor + i)%50 == 0:
            x_lower_bound_minor = x_lower_bound_minor + i
            break

    y_lower_bound_major = y_low
    y_lower_bound_minor = y_low
    for i in range(10):
        if (y_lower_bound_major + i)%10 == 0:
            y_lower_bound_major = y_lower_bound_major + i
            break
    for i in range(5):
        if (y_lower_bound_minor + i)%5 == 0:
            y_lower_bound_minor = y_lower_bound_minor + i
            break

    print(x_lower_bound_minor)
    print(x_lower_bound_major)

    major_x_ticks = np.arange(x_lower_bound_major, x_up, 100)
    minor_x_ticks = np.arange(x_lower_bound_minor, x_up, 50)
    major_y_ticks = np.arange(y_lower_bound_major, y_up, 10)
    minor_y_ticks = np.arange(y_lower_bound_minor, y_up, 5)

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

def save_plot(filename):
    plt.savefig('plots/' + filename + '.png', dpi=200)