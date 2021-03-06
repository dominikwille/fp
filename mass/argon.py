#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

plots = [
    ('Left over gas', 'Gr10/restgasmessung2', [1,2.75,15,16,17,18,26,27,28,29,31,39,41,43,44,57], 60, 5e-4),
    ('Luft', 'Gr10/Testgas Luft 1', [1,2.75,12,14,15,16,17,18,20,26,27,28,29,30,32,40,41,42,43,44,57], 60, 5e-4),
    ('Argon', 'Gr10/Testgas 1 Argon', [1,2.75,16,17,18,20,26,27,28,29,32,39.9,41,43,44,57], 60, 5e-4),
    ('Ethanol', 'Gr10/Testgas 2 Ethanol', [1,2.75,12,13,14,15,16,17,18,25,26,27,28,29,30,32,37,38,39,40,41,42,43,44,57,58], 60, 5e-3),
    ('Aceton', 'Gr10/Testgas 2 Aceton', [1,2.75,12,13,14,15,16,17,18,25,26,27,28,29,30,31,32,37,38,39,40,41,42,43,44,57,58], 60, 5e-4),
]

def special(x):
    if(int(round(x)) != int(x) and abs(round(x) - x) <= 0.2):
        return int(x) + 1
    return int(x)

def readxy(filename, x_max):
    x = []
    y = []

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            try:
                x_ = float(str(row[0]).replace(',', '.')) - 0.4
                y_ = -float(str(row[1]).replace(',', '.'))
                if(x >= 0 and x_ <= x_max):
                    x.append(x_)
                    y.append(y_)
            except:
                print str(row[0]).replace(',', '.')
                print str(row[1]).replace(',', '.')
    return (x, y)

def x2index(x):
    return int(x*10 +3)

def make_graph(n):
    title, filename, points, x_max, preasure = plots[n]
    x, y = readxy(filename, x_max)

    plt.plot(x, y)
    i = 0;
    for p in points:
        plt.text(p, y[x2index(p)] + 0.01 * max(y), str(special(p)), horizontalalignment='center', fontsize=8)
    plt.xlim([0,x_max])
    plt.xlabel('${m}/{q}$ in $\\left[{\\mathrm{amu}}/{\\mathrm{e_0}}\\right]$', fontsize=12)
    plt.ylabel('Measured intensity')
    plt.ylim([-0.05,4])
    plt.title(title)
    plt.show()

def make_table():
    i = 0
    I = 0
    P = []
    title, filename, points, x_max, preasure = plots[2]
    x, y = readxy(filename, x_max)
    end = special(max(points))
    for p in points:
        I += y[x2index(p)]
    
    for 
    print I

make_graph(2)
make_table()
