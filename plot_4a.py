import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import import_data_4a, plot_axes_4, save_plot

years, averages = import_data_4a()

fig, ax = plot_axes_4()



for i in range(len(averages)):
    #print(len(years[i]), len(averages[i]))
    ax.plot(years[i], averages[i])

save_plot('4a')

