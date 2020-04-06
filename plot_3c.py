import matplotlib.pyplot as plt
import numpy as np
from utils import import_data_3, plot_axes_3, save_plot

countries, average_temp_celsius = import_data_3()

fig, ax = plot_axes_3()
ax.set_xticks(np.arange(1, 9, 1))
ax.set_xticklabels(countries)
plt.violinplot(average_temp_celsius, showmeans=False, showmedians=False, showextrema=False, widths=0.8)

save_plot('3c')