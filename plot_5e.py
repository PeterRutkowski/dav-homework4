from utils import import_cities, save_plot
import matplotlib.pyplot as plt
import numpy as np

data = import_cities()

country_codes = ['Brazil', 'France', 'Japan', 'New Zealand', 'Poland', 'South Africa', 'Sweden', 'Ukraine']
city_codes = [['Brasília','Canoas'],['Paris','Marseille'],['Tokyo','Tottori'],
              ['Auckland','Hamilton'],['Warsaw','Wroclaw'],['Cape Town','Johannesburg'],
              ['Stockholm','Uppsala'],['Kiev','Lvov','Odesa','Kherson']]
colors = [(51, 102, 204),(0, 0, 153),(51, 153, 102),(0, 51, 0),(153, 255, 102),(204, 204, 0),
          (153, 153, 102),(102, 51, 0),(255, 153, 0),(204, 51, 0),(255, 140, 102),(255, 51, 204),
          (255, 179, 236),(204, 0, 255),(102, 0, 204),(255, 255, 153),(128, 128, 0),(77, 195, 255)]
colors = np.divide(colors, 255)

years, averages = [], []
for i in range(8):
    years.append([])
    averages.append([])
    for j in range(len(city_codes[i])):
        years[i].append([])
        averages[i].append([])

for i in range(len(data)):
    for j in range(len(city_codes)):
        for k in range(len(city_codes[j])):
            if len(data[i][j][k]) > 0:
                years[j][k].append(1743+i)
                averages[j][k].append(data[i][j][k])

fig, ax = plt.subplots(3, 3)
title_font = {'fontname':'Times New Roman',
        'weight' : 'bold',
        'size'   : 25}
plt.suptitle(t='Average temperature',x=0.42, y=0.95, va='center', ha='center', **title_font)

ax[-1, 0].set_xlabel('.', color=(0, 0, 0, 0))
ax[-1, 0].set_ylabel('.', color=(0, 0, 0, 0))
fig.text(0.42, 0.02, 'Year of observation', va='center', ha='center', size=15)
fig.text(0.04, 0.5, 'Average temperature', va='center', ha='center', rotation='vertical', size=15)

plot11 = ax[0,0].plot(years[0][0], averages[0][0], linewidth=1., label=city_codes[0][0], color=colors[0])
plot12 = ax[0,0].plot(years[0][1], averages[0][1], linewidth=1., label=city_codes[0][1], color=colors[1])
plot21 = ax[0,1].plot(years[1][0], averages[1][0], linewidth=1., label=city_codes[1][0], color=colors[2])
plot22 = ax[0,1].plot(years[1][1], averages[1][1], linewidth=1., label=city_codes[1][1], color=colors[3])
plot31 = ax[0,2].plot(years[2][0], averages[2][0], linewidth=1., label=city_codes[2][0], color=colors[4])
plot32 = ax[0,2].plot(years[2][1], averages[2][1], linewidth=1., label=city_codes[2][1], color=colors[5])
plot41 = ax[1,0].plot(years[3][0], averages[3][0], linewidth=1., label=city_codes[3][0], color=colors[6])
plot42 = ax[1,0].plot(years[3][1], averages[3][1], linewidth=1., label=city_codes[3][1], color=colors[7])
plot51 = ax[1,1].plot(years[4][0], averages[4][0], linewidth=1., label=city_codes[4][0], color=colors[8])
plot52 = ax[1,1].plot(years[4][1], averages[4][1], linewidth=1., label=city_codes[4][1], color=colors[9])
plot61 = ax[1,2].plot(years[5][0], averages[5][0], linewidth=1., label=city_codes[5][0], color=colors[10])
plot62 = ax[1,2].plot(years[5][1], averages[5][1], linewidth=1., label=city_codes[5][1], color=colors[11])
plot71 = ax[2,0].plot(years[6][0], averages[6][0], linewidth=1., label=city_codes[6][0], color=colors[12])
plot72 = ax[2,0].plot(years[6][1], averages[6][1], linewidth=1., label=city_codes[6][1], color=colors[13])
plot81 = ax[2,1].plot(years[7][0], averages[7][0], linewidth=1., label=city_codes[7][0], color=colors[14])
plot82 = ax[2,1].plot(years[7][1], averages[7][1], linewidth=1., label=city_codes[7][1], color=colors[15])
plot83 = ax[2,1].plot(years[7][2], averages[7][2], linewidth=1., label=city_codes[7][2], color=colors[16])
plot84 = ax[2,1].plot(years[7][3], averages[7][3], linewidth=1., label=city_codes[7][3], color=colors[17])

def background(ax, label, xticks=0, yticks=0):
    ax.text(0.5, 1.08, label, va='center', ha='center', size=12, color='black', transform=ax.transAxes)

    ax.set_ylim(-7, 25)
    ax.set_xlim(1730, 2025)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['top'].set_color((0.7, 0.7, 0.7))
    ax.spines['bottom'].set_color((0.7, 0.7, 0.7))
    ax.spines['right'].set_color((0.7, 0.7, 0.7))
    ax.spines['left'].set_color((0.7, 0.7, 0.7))

    major_x_ticks = np.arange(1800, 2025, 100)
    minor_x_ticks = np.arange(1750, 2025, 50)
    major_y_ticks = np.arange(-5, 25, 5)
    minor_y_ticks = np.arange(-5, 25, 2.5)

    ax.set_xticks(major_x_ticks)
    ax.set_xticks(minor_x_ticks, minor=True)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)

    ax.tick_params(axis='x', which='major', colors='black', labelsize=11.0, length=3.0, rotation=-45)
    ax.tick_params(axis='x', which='minor', colors='black', labelsize=11.0, length=0)
    ax.tick_params(axis='y', which='major', colors='black', labelsize=11.0, length=3.0)
    ax.tick_params(axis='y', which='minor', colors='black', labelsize=11.0, length=0)

    ax.grid(True, zorder=0, color=(0.88,0.88,0.88), which='minor', linewidth=0.1)
    ax.grid(True, zorder=0, color=(0.88,0.88,0.88), which='major', linewidth=0.5)

    if xticks == 0:
        ax.set_xticklabels([])
        ax.tick_params(axis='x', which='major', colors='black', labelsize=8.0, length=0)
        ax.tick_params(axis='x', which='minor', colors='black', labelsize=8.0, length=0)

    if yticks == 0:
        ax.set_yticklabels([])
        ax.tick_params(axis='y', which='major', colors='black', labelsize=8.0, length=0)
        ax.tick_params(axis='y', which='minor', colors='black', labelsize=8.0, length=0)

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

plt.subplots_adjust(right=0.75)

plots = [plot11,plot12,plot21,plot22,plot31,plot32,plot41,plot42,plot51,
         plot52,plot61,plot62,plot71,plot72,plot81,plot82,plot83,plot84]

labels = []
for i in range(len(city_codes)):
    for j in range(len(city_codes[i])):
        labels.append(city_codes[i][j])
sorted_indices = np.argsort(labels)
sorted_plots = plots[sorted_indices[0]]
sorted_labels = [labels[sorted_indices[0]]]
for i in range(1,len(sorted_indices)):
    sorted_plots = sorted_plots + plots[sorted_indices[i]]
    sorted_labels.append(labels[sorted_indices[i]])

plt.legend(sorted_plots, sorted_labels, loc='center left', bbox_to_anchor=(1.0, 1.7),
           title='City', prop={'size': 12}, frameon=False)

save_plot('5e')