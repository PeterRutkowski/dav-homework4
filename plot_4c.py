from utils import import_data_4, plot_axes_4, save_plot
import matplotlib.pyplot as plt

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

country_codes = ['Brazil', 'France', 'Japan', 'New Zealand', 'Poland', 'South Africa', 'Sweden', 'Ukraine']
colors = [(1,0,0), (1,0,1), (0,1,0), (0,0,1), (1,1,0), (0,1,1), (0,0,0), (1,0.5,0)]

for i in range(len(averages)):
    ax.plot(years[i], averages[i], linewidth=1.2, label=country_codes[i], color=colors[i])

plt.subplots_adjust(right=0.76)
plt.legend(bbox_to_anchor=(1.,0.5), loc='center left', frameon=False, title='Country')

save_plot('4c')