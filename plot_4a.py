from utils import import_data_4, plot_axes_4, save_plot
import numpy as np

data = import_data_4()
years, averages = [], []
for i in range(len(data)):
    for j in range(len(data[0])):
        if len(data[i][j]) > 0:
            years.append(1743 + i)
            averages.append(np.average(data[i][j]))

fig, ax = plot_axes_4()

ax.plot(years, averages, color='black')

save_plot('4a')