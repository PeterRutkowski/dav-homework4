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
colors = [(1,0,0), (1,0,1), (0,1,0), (0,0,1), (1,1,0), (0,1,1), (0,0,0), (1,0.5,0)]

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3)

ax1.plot(years[0], averages[0], linewidth=1.2, label=country_codes[0], color=colors[0])
ax2.plot(years[1], averages[1], linewidth=1.2, label=country_codes[1], color=colors[1])
ax3.plot(years[2], averages[2], linewidth=1.2, label=country_codes[2], color=colors[2])
ax4.plot(years[3], averages[3], linewidth=1.2, label=country_codes[3], color=colors[3])
ax5.plot(years[4], averages[4], linewidth=1.2, label=country_codes[4], color=colors[4])
ax6.plot(years[5], averages[5], linewidth=1.2, label=country_codes[5], color=colors[5])
ax7.plot(years[6], averages[6], linewidth=1.2, label=country_codes[6], color=colors[6])
ax8.plot(years[7], averages[7], linewidth=1.2, label=country_codes[7], color=colors[7])


def background(ax):

    ax.set_facecolor((0.88, 0.88, 0.88))
    ax.set_ylim(-5, 22)
    ax.set_xlim(1730, 2025)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    major_x_ticks = np.arange(1800, 2025, 100)
    minor_x_ticks = np.arange(1750, 2025, 50)
    major_y_ticks = np.arange(0, 22, 5)
    minor_y_ticks = np.arange(-5, 22, 2.5)

    ax.set_xticks(major_x_ticks)
    ax.set_xticks(minor_x_ticks, minor=True)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    plt.grid(True, zorder=0, color='white')
    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.4)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=1)

background(ax1)
background(ax2)
background(ax3)
background(ax4)
background(ax5)
background(ax6)
background(ax7)
background(ax8)

ax9.spines['top'].set_visible(False)
ax9.spines['bottom'].set_visible(False)
ax9.spines['right'].set_visible(False)
ax9.spines['left'].set_visible(False)
ax9.grid(False)
#ax9.set_xticks([])


plt.tight_layout()



save_plot('5a')