#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def lin(x, m, n):
    return m*x+n

x = []
y = []
y_err = []
with open('peaks.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        s = str(row[0]).strip()
        t = str(row[1]).strip()
        u = str(row[2]).strip()
        try:
            x.append(float(s))
            y.append(float(t))
            y_err.append(float(s))
        except:
            print row

x[2] = x[2]/2
x = np.asarray(x)
y = np.asarray(y)
y_err = np.asarray(y_err)
print x
print y

mean = 6000
sigma = 250

# popt,pcov = curve_fit(lin,x,y,p0=[1.0,0])

# d_x0 = pcov[1,1]
# a = popt[0]
# x0 = popt[1]
# sigma = popt[2]

x_ = range(0,8000)

# plt.text(x0, a * 1.2 + 27, text, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')

plt.errorbar(x, y, xerr=0.1, yerr=0.01)

# plt.plot(x_,lin(x_,*popt),'r',label='fit')
plt.xlabel('channel #')
plt.ylabel('Energy')

plt.tight_layout()
plt.show()

