#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

start = [
    ('137cskal.Spe', 167, 196, 1100, 1200, 9000, True),
    ('137cskal.Spe', 196, 220, 190, 1200, 9000, True),
    ('137cskal.Spe', 403, 416, 140, 1200, 9000, True),
    ('137cskal.Spe', 416, 428, 140, 1200, 9000, True),
    ('137cskal.Spe', 3600, 3800, 800, 1200, 9000, True),
    ('22nakal.Spe', 2851, 2960, 35, 40, 9000, True),
    ('22nakal.Spe', 7133, 7168, 8, 40, 9000, True),
    ('241amkal.Spe', 71, 87, 38000, 45000, 1000, True),
    ('241amkal.Spe', 87, 112, 38000, 45000, 1000, True),
    ('241amkal.Spe', 112, 133, 38000, 45000, 1000, True),
    ('241amkal.Spe', 140, 160, 38000, 45000, 1000, True),
    ('241amkal.Spe', 317, 350, 38000, 45000, 1000, True),
    ('60cokal.Spe', 6544, 6611, 90, 200, 9000, True),
    ('60cokal.Spe', 7437, 7500, 70, 200, 9000, True),
    ('Co_long.Spe', 7437, 7500, 70, 200, 9000, False),
]

filename, x_min, x_max, y_max, y_range, x_range, fit = start[12]

x = []
y = []
ye = []
i = 0.0
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        s = str(row[0]).strip()
        if(s.isdigit()):
            x.append(i)
            y.append(int(s))
            i += 1.0

x = np.asarray(x)
y = np.asarray(y)

x_ = x[x_min:x_max]
y_ = y[x_min:x_max]

plt.errorbar(x, y, xerr=0.1, yerr=0.01)

if(fit):
    popt,pcov = curve_fit(gaus,x_,y_,p0=[y_max, (x_max+x_min)/2.0, (x_max-x_min)/2.0])
    
    print pcov
    d_x0 = pcov[1,1]
    d_sigma = pcov[2,2]
    d_a = pcov[0,0]
    a = popt[0]
    x0 = popt[1]
    sigma = popt[2]

    text = r'$x_0 =\, ' + str(round(x0, 2)) + '\pm ' + str(round(np.sqrt(d_x0), 2))  + '$'
    text2 =  r'$\sigma =\, ' + str(round(abs(sigma), 2)) + '\pm ' + str(round(np.sqrt(d_sigma), 2))  + '$'
    text3 =  r'$a =\, ' + str(round(abs(a), 2)) + '\pm ' + str(round(np.sqrt(d_a), 2))  + '$'
    
    plt.text(x0, y_max + 0.01 * y_range, text, horizontalalignment='center')
    plt.text(x0, y_max + 0.05 * y_range, text2, horizontalalignment='center')
    plt.text(x0, y_max + 0.09 * y_range, text3, horizontalalignment='center')

    plt.plot(x_,gaus(x_,*popt),'r',label='fit')

plt.ylim([0,y_range])
plt.xlim([0,x_range])
plt.xlabel('channel #')
plt.ylabel('detected decays')

plt.tight_layout()
plt.show()

