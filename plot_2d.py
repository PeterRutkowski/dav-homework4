import matplotlib.pyplot as plt
from utils import import_data_2, plot_axes_2, save_plot

years, average_temp_celsius = import_data_2()

fig, ax = plot_axes_2()

fig = plt.scatter(years, average_temp_celsius, alpha=0.15, edgecolor=(0.07, 0.215, 1, 1),
                  facecolors=(0.07, 0.215, 1, 1), s=5, zorder=3)

save_plot('2d')