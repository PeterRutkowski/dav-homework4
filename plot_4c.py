from utils import import_data_4a, plot_axes_4, save_plot

years, averages = import_data_4a()

fig, ax = plot_axes_4()

for i in range(len(averages)):
    ax.plot(years[i], averages[i], linewidth=1.2)

save_plot('4c')

