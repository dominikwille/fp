#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

x = []
y = []
ye = []
i = 0
with open('22nacal.Spe', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        s = str(row[0]).strip()
        if(s.isdigit()):
            x.append(i)
            y.append(int(s))
            i += 1

x = np.asarray(x)
y = np.asarray(y)


x_ = x[5200:6100]
y_ = y[5200:6100]

mean = 6000
sigma = 250

popt,pcov = curve_fit(gaus,x_,y_,p0=[1,mean,sigma])

d_x0 = pcov[1,1]
a = popt[0]
x0 = popt[1]
sigma = popt[2]

text = r'$x_0 =\, ' + str(round(x0, 2)) + '\pm ' + str(round(np.sqrt(d_x0), 2))  + '$'#;\,\, \sigma =' + str(abs(round(sigma, 2))) + '$'
plt.text(x0, a * 1.2 + 27, text, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')

plt.errorbar(x, y, xerr=0.1, yerr=0.01)
plt.plot(x_,gaus(x_,*popt),'r',label='fit')
plt.xlabel('channel #')
plt.ylabel('detected decays')

plt.tight_layout()
plt.show()

