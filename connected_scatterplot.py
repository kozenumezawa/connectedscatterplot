# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

f = open('./csv/kyoto_kisyotyo.csv', 'r')
reader = csv.reader(f)
header = next(reader)
time = []
velocity = []
temperature = []
rainfall = []
humidity = []

for row in reader:
    time.append(int(row[0]))
    velocity.append(float(row[1]))
    temperature.append(float(row[2]))
    rainfall.append(float(row[3]))
    humidity.append(float(row[4]))

# plt.plot(time, temperature, color='b', lw=1)
# plt.plot(time, humidity, color='g', lw=2)
# plt.show()
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(temperature, humidity, time, label='parametric curve')
# ax.legend()
# plt.show()

plt.subplot(2,1,1)
plt.plot(time[0:20], temperature[0:20], color='b', lw=1)
plt.plot(time[0:20], humidity[0:20], color='g', lw=2)
plt.subplot(2,1,2)
plt.plot(temperature[0:20], humidity[0:20], '.r-')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(temperature[0:20], humidity[0:20], time[0:20], label='parametric curve')
ax.legend()
plt.show()
