import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/temperature_clean.csv")
years = np.asarray(data['year'])
average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
del data

plt.scatter(years, average_temp_celsius, edgecolor=((0, 0, 0, 1)), facecolors='none')

plt.ylabel('AverageTemperatureCelsius')
plt.xlabel('year')
plt.tight_layout()
plt.ylim(-18, 32)
plt.xlim(1730, 2025)
plt.xticks(np.arange(start=1750,stop=2050, step=50))
plt.yticks(np.arange(start=-10, stop=32, step=10), rotation='vertical')
plt.savefig('plots/2a.png', dpi=200)
plt.clf()