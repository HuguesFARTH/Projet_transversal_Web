import numpy as np
import time
import matplotlib.pyplot as plt
from rplidar import RPLidar
import math
import json

try:
    
    lidar = RPLidar('/dev/ttyUSB0')

    info = lidar.get_info()
    print(info)

    health = lidar.get_health()
    print(health)
except:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    lidar = RPLidar('/dev/ttyUSB0')
    info = lidar.get_info()
    print(info)
    health = lidar.get_health()
    print(health)
datas = {}

plt.ion()
figure, ax = plt.subplots(figsize=(8,6))

plt.xlabel("y",fontsize=18)
plt.ylabel("x",fontsize=18)
x_max = 1000
plt.xlim([-x_max, x_max])
y_max = 1000
plt.ylim([-y_max, y_max])

amount_max = 3
for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    x = np.zeros(len(scan))
    y = np.zeros(len(scan))
    print(scan[0])
    for j,val in enumerate(scan):
        x[j] = (math.cos(val[1]*math.pi/180)*val[2])
        y[j] = (-math.sin(val[1]*math.pi/180)*val[2])
    datas[str(i)] = [x,y]
    for j in range(1,len(ax.get_lines())):
        c = ax.get_lines()[j].get_color()
        c[3] -= 1/amount_max
        ax.get_lines()[j].set_color(c)

    if i >= amount_max:
      ax.lines[0].remove()
    line = ax.plot(x,y, c=[1,0,0,1])
    figure.canvas.draw()
    figure.canvas.flush_events()
    if i > 400:
        break


    #scatter = ax.scatter(x,y, marker="*", s=1)
    #figure.canvas.draw()
    #figure.canvas.flush_events()

with open("datas.txt", "w") as fp:
    json.dump(datas,fp)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
