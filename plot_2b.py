import matplotlib.pyplot as plt
from utils import import_AvTempCelsius, plot_background, save_plot

years, average_temp_celsius = import_AvTempCelsius()

fig, ax = plot_background(1730, 2025, -18, 32)

fig = plt.scatter(years, average_temp_celsius, edgecolor=((0, 0, 0, 1)),
                  facecolors=((0, 0, 0, 1)), s=5, zorder=3)

save_plot('2b')