import matplotlib.pyplot as plt
from utils import import_data_4, save_plot
import numpy as np

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

country_codes = ['Brazil', 'France', 'Japan', 'New Zealand', 'Poland', 'South Africa', 'Sweden', 'Ukraine']
colors = [(1,0,0), (1,0,1), (0.5,0.5,0.5), (0.5,0.1,0.5), (0.4,0,1), (0,0.7,1), (0,0,0), (1,0.5,0)]

fig, ax = plt.subplots(3, 3)

ax[-1, 0].set_xlabel('.', color=(0, 0, 0, 0))
ax[-1, 0].set_ylabel('.', color=(0, 0, 0, 0))
fig.text(0.42, 0.04, 'year', va='center', ha='center')
fig.text(0.04, 0.5, 'countryAverage', va='center', ha='center', rotation='vertical')

plot1 = ax[0,0].plot(years[0], averages[0], linewidth=1.2, label=country_codes[0], color=colors[0])
plot2 = ax[0,1].plot(years[1], averages[1], linewidth=1.2, label=country_codes[1], color=colors[1])
plot3 = ax[0,2].plot(years[2], averages[2], linewidth=1.2, label=country_codes[2], color=colors[2])
plot4 = ax[1,0].plot(years[3], averages[3], linewidth=1.2, label=country_codes[3], color=colors[3])
plot5 = ax[1,1].plot(years[4], averages[4], linewidth=1.2, label=country_codes[4], color=colors[4])
plot6 = ax[1,2].plot(years[5], averages[5], linewidth=1.2, label=country_codes[5], color=colors[5])
plot7 = ax[2,0].plot(years[6], averages[6], linewidth=1.2, label=country_codes[6], color=colors[6])
plot8 = ax[2,1].plot(years[7], averages[7], linewidth=1.2, label=country_codes[7], color=colors[7])

def background(ax, label, xticks=0, yticks=0):
    ax.set_title(label, size=10)

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_ylim(-5, 23)
    ax.set_xlim(1730, 2025)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    major_x_ticks = np.arange(1800, 2025, 100)
    minor_x_ticks = np.arange(1750, 2025, 50)
    major_y_ticks = np.arange(0, 23, 5)
    minor_y_ticks = np.arange(-5, 23, 2.5)

    ax.set_xticks(major_x_ticks)
    ax.set_xticks(minor_x_ticks, minor=True)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', which='major', colors='grey', labelsize=8.0, length=3.0)
    ax.tick_params(axis='x', which='minor', colors='grey', labelsize=8.0, length=0)
    ax.tick_params(axis='y', which='major', colors='grey', labelsize=8.0, length=3.0)
    ax.tick_params(axis='y', which='minor', colors='grey', labelsize=8.0, length=0)

    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.3)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=0.8)

    if xticks == 0:
        ax.set_xticklabels([])
        ax.tick_params(axis='x', which='major', colors='grey', labelsize=8.0, length=0)
        ax.tick_params(axis='x', which='minor', colors='grey', labelsize=8.0, length=0)

    if yticks == 0:
        ax.set_yticklabels([])
        ax.tick_params(axis='y', which='major', colors='grey', labelsize=8.0, length=0)
        ax.tick_params(axis='y', which='minor', colors='grey', labelsize=8.0, length=0)

background(ax[0,0], country_codes[0], yticks=1)
background(ax[0,1], country_codes[1])
background(ax[0,2], country_codes[2])
background(ax[1,0], country_codes[3], yticks=1)
background(ax[1,1], country_codes[4])
background(ax[1,2], country_codes[5])
background(ax[2,0], country_codes[6], xticks=1, yticks=1)
background(ax[2,1], country_codes[7], xticks=1)

ax[2,2].spines['top'].set_visible(False)
ax[2,2].spines['bottom'].set_visible(False)
ax[2,2].spines['right'].set_visible(False)
ax[2,2].spines['left'].set_visible(False)
ax[2,2].grid(False)
ax[2,2].set_xticks([])
ax[2,2].set_yticks([])

plt.tight_layout()
plt.subplots_adjust(right=0.75)

plots = plot1+plot2+plot3+plot4+plot5+plot6+plot7+plot8
labels = [plot.get_label() for plot in plots]
plt.legend(plots, labels, loc='center left', bbox_to_anchor=(1.05, 1.7), title='Country', prop={'size': 10})

save_plot('5a')