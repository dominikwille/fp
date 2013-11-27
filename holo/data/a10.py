"""
Demo of the errorbar function.
"""
import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
ye = []

with open('holo_a10.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]) * 100.0)
        ye.append(float(row[2]))

x = np.asarray(x)
y = np.asarray(y)


plt.errorbar(x, y, xerr=1., yerr=ye)
plt.xlabel('$\Delta x$ [$cm$]')
plt.ylabel('$I$ [$\%$]')
plt.show()

