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
x_err = []
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
            x_err.append(float(u))
        except:
            print row

x[2] = x[2]/2
x = np.asarray(x)
y = np.asarray(y)
x_err = np.asarray(x_err)

mean = 6000
sigma = 250

popt,pcov = curve_fit(lin,x,y,p0=[1.0,0])

# d_x0 = pcov[1,1]
# a = popt[0]
# x0 = popt[1]
# sigma = popt[2]

x_ = range(0,8000)
x_ = np.asarray(x_)
text = '$m = ' + str(round(popt[0], 5)) + '\pm' +  str(round(pcov[0,0], 5)) + '$'
text2 = '$n = ' + str(round(popt[1], 5)) + '\pm' +  str(round(pcov[1,1], 5)) + '$'
plt.text(2000, 1000, text, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')
plt.text(2000, 935, text2, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')

print popt

plt.errorbar(x, y, xerr=x_err, fmt='+')

plt.plot(x_,lin(x_, popt[0], popt[1]),'r',label='fit')
plt.xlabel('channel #')
plt.ylabel('Energy  [$keV$]')
plt.ylim([0,2000])
plt.tight_layout()
plt.show()

