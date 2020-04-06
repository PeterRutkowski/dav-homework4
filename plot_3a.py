import matplotlib.pyplot as plt
from utils import import_data_3, plot_axes_3,save_plot

countries, average_temp_celsius = import_data_3()

fig, ax = plot_axes_3()

plt.boxplot(average_temp_celsius, labels=countries, zorder=3, patch_artist=True,
           boxprops=dict(facecolor='white', color='black'), capprops=dict(color='black'),
           whiskerprops=dict(color='black'),
           flierprops=dict(markerfacecolor='black', markeredgecolor='black', markersize=3),
           medianprops=dict(color='black'),)

save_plot('3a')