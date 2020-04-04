import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plot all AverageTemperatureCelsius vs. year

# import data
data = pd.read_csv("data/temperature_clean.csv")
years = np.asarray(data['year'])
average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
del data

colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']
plt.scatter(years, average_temp_celsius, edgecolor=((0, 0, 0, 1)), facecolors=((0, 0, 0, 1)), s=)

plt.ylabel('AverageTemperatureCelsius')
plt.xlabel('temperature_complete')
plt.tight_layout()
plt.ylim(-18, 32)
plt.xlim(1730, 2025)
plt.xticks(np.arange(start=1750,stop=2050, step=50))
plt.yticks(np.arange(start=-10, stop=32, step=10), rotation='vertical')
plt.savefig('plots/2b.png', dpi=200)
plt.clf()



