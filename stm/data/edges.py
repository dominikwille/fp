#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

edges = [150, 300, 350, 350, 400, 700, 700, 900, 1100, 1100, 0]
x = [0,1,2,3,4,5,6,7,8,9, 10]

y1 = [350, 350]
y2 = [700, 700]
y3 = [1050, 1050]
x_ = [0, 10]

plt.plot(x, edges, 'o')
plt.plot(x_, y1)
plt.plot(x_, y2)
plt.plot(x_, y3)
plt.xlabel('#')
plt.ylabel('height in pm')
plt.show()
