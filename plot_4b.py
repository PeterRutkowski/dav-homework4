from utils import import_data_4, plot_axes_4, save_plot

data = import_data_4()
years, averages = [], []
for i in range(8):
    years.append([])
    averages.append([])

for i in range(len(data)):
    for j in range(len(data[0])):
        if len(data[i][j]) > 0:
            years[j].append(1743+i)
            averages[j].append(data[i][j])

fig, ax = plot_axes_4()

for i in range(len(averages)):
    ax.plot(years[i], averages[i], color='black', linewidth=1.2)

save_plot('4b')