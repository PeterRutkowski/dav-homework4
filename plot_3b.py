import numpy as np
import matplotlib.pyplot as plt
from utils import import_data_3, plot_axes_3, save_plot

countries, average_temp_celsius = import_data_3()

fig, ax = plot_axes_3()

plt.boxplot(average_temp_celsius, labels=countries, zorder=3, patch_artist=True,
           boxprops=dict(facecolor='none', color='black'), capprops=dict(color='black'),
           whiskerprops=dict(color='black'),
           flierprops=dict(markerfacecolor='black', markeredgecolor='black', markersize=3),
           medianprops=dict(color='black'),)

scatter_distribution = []
for i in range(len(average_temp_celsius)):
    scatter = []
    for j in range(len(average_temp_celsius[i])):
        scatter.append(np.random.uniform(i + 1 - 0.28, i + 1 + 0.28))
    scatter_distribution.append(scatter)

for x, y in zip(scatter_distribution, average_temp_celsius):
    plt.scatter(x, y, c='orange', alpha=0.1, zorder=3, s=5)

save_plot('3b')