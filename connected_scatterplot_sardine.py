# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D
mpl.rcParams['legend.fontsize'] = 10

f = open('./csv/sardine_anchovy_sst.csv', 'r')
reader = csv.reader(f)
header = next(reader)
time = []
anchovy = []
np_sst = []


for row in reader:
    time.append(int(row[0]))
    anchovy.append(float(row[1]))
    np_sst.append(float(row[4]))

# plt.plot(time, anchovy, color='b', lw=1)
# plt.plot(time, np_sst, color='g', lw=2)
# plt.show()
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(anchovy, np_sst, time, label='parametric curve')
# ax.legend()
# plt.show()

plt.subplot(2,1,1)
plt.plot(time[0:20], anchovy[0:20], color='b', lw=1)
plt.plot(time[0:20], np_sst[0:20], color='g', lw=2)
plt.subplot(2,1,2)
plt.plot(anchovy[0:20], np_sst[0:20], '.r-')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(anchovy[0:20], np_sst[0:20], time[0:20], label='parametric curve')
ax.legend()
plt.show()
