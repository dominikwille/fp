#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
with open('dats.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        s = str(row[0]).strip()
        t = str(row[1]).strip()
        u = str(row[2]).strip()
        try:
            y.append(float(s))
            x.append(float(t))
            z.append(u)
        except:
            print row

x = np.asarray(x)
y = np.asarray(y)
z = np.asarray(z)


x_ = range(0,30)
x_ = np.asarray(x_)

# d_m = np.sqrt(pcov[0,0])
# d_n = np.sqrt(pcov[1,1])
# d_o = np.sqrt(pcov[2,2])

# text = '$m = (' + str(int(round(popt[0], -4))) + '\pm' +  str(int(round(np.sqrt(pcov[0,0]), -4))) + ')$'
# text2 = '$n = (' + str(round(popt[1], 5)) + '\pm' +  str(round(np.sqrt(pcov[1,1]), 5)) + ')\, 1/mm$'
# text3 = '$o = (' + str(int(round(popt[2], -4))) + '\pm' +  str(int(round(np.sqrt(pcov[2,2]), -4))) + ')$'

# plt.text(20, 3800000, text, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')
# plt.text(20, 3750000, text2, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')
# plt.text(20, 3850000, text3, horizontalalignment='center')#, verticalalignment='bottom' , rotation='vertical')

print z
i = 0
for i in range(4):
    plt.text(x[i], y[i], ' ' + z[i])

print x
print y
plt.errorbar(x, y, yerr=np.sqrt(y), fmt='+')


plt.xlabel('Atomic number')
plt.ylabel('Ratio of absorbtion')
# plt.ylim([0,2000])
plt.xlim([49, 54])
plt.tight_layout()
plt.show()
