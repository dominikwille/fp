#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def lin(x, m, n, o):
    return m*np.exp(-n*x) + o

x = []
y = []
x_err = []
with open('Pb.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        s = str(row[0]).strip()
        t = str(row[1]).strip()
        # u = str(row[2]).strip()
        try:
            y.append(float(s))
            x.append(float(t))
            # x_err.append(float(u))
        except:
            print row

x = np.asarray(x)
y = np.asarray(y)
# x_err = np.asarray(x_err)

popt,pcov = curve_fit(lin,x,y,p0=[3000000, 0.003, 100000])

print pcov

x_ = range(0,30)
x_ = np.asarray(x_)

d_m = np.sqrt(pcov[0,0])
d_n = np.sqrt(pcov[1,1])
d_o = np.sqrt(pcov[2,2])

text = '$m = (' + str(int(round(popt[0], -4))) + '\pm' +  str(int(round(np.sqrt(pcov[0,0]), -4))) + ')$'
text2 = '$n = (' + str(round(popt[1], 5)) + '\pm' +  str(round(np.sqrt(pcov[1,1]), 5)) + ')\, 1/mm$'
text3 = '$o = (' + str(int(round(popt[2], -4))) + '\pm' +  str(int(round(np.sqrt(pcov[2,2]), -4))) + ')$'

plt.text(20, 4000000, text, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')
plt.text(20, 3900000, text2, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')
plt.text(20, 3800000, text3, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')


print popt

print d_o

plt.errorbar(x, y, yerr=np.sqrt(y), fmt='+')

plt.plot(x_,lin(x_, popt[0], popt[1], popt[2]),'r',label='fit')
plt.plot(x_,lin(x_, popt[0] - d_m, popt[1] + d_n, popt[2] - d_o),'r--')
plt.plot(x_,lin(x_, popt[0] + d_m, popt[1] - d_n, popt[2] + d_o),'r--')

plt.xlabel('Width [$mm$]')
plt.ylabel('Decays [1]')
# plt.ylim([0,2000])
plt.tight_layout()
plt.show()
