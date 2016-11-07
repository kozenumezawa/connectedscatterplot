# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

f = open('./csv/logistic_0_0.csv', 'r')
reader = csv.reader(f)
time = []
x = []
y = []
for row in reader:
    time.append(int(row[0]))
    x.append(float(row[1]))
    y.append(float(row[2]))

plt.subplot(2,1,1)
plt.plot(time[0:20], x[0:20], color='b', lw=1)
plt.plot(time[0:20], y[0:20], color='g', lw=2)
plt.subplot(2,1,2)
plt.plot(x[0:20], y[0:20], '.r-')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x[0:20], y[0:20], time[0:20], label='parametric curve')
ax.legend()
plt.show()
