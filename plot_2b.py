import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/temperature_clean.csv")
years = np.asarray(data['year'])
average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
del data

fig, ax = plt.subplots()
fig = plt.scatter(years, average_temp_celsius, edgecolor=((0, 0, 0, 1)), facecolors=((0, 0, 0, 1)), s=5, zorder=3)

ax.set_facecolor((0.88,0.88,0.88))
ax.set_ylim(-18, 32)
ax.set_xlim(1730, 2025)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

major_x_ticks = np.arange(1800, 2050, 100)
minor_x_ticks = np.arange(1750, 2050, 50)
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

plt.savefig('plots/2b.png', dpi=200)
plt.clf()