import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plot all AverageTemperatureCelsius vs. year

# import data
data = pd.read_csv("data/data_I_A.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))


