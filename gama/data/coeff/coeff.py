#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import csv

Al = [
    (3, 'Al_3mm.Spe'),
    (6, 'Al_6mm.Spe'),
    (9, 'Al_9mm.Spe'),
    (12, 'Al_12mm.Spe'),
    (15, 'Al_15mm.Spe'),
    (18 ,'Al_18mm.Spe'),
    (21, 'Al_21mm.Spe')
]

Cu = [
    (2, 'Cu_2mm.Spe'),
    (4, 'Cu_4mm.Spe'),
    (6, 'Cu_6mm.Spe'),
    (8, 'Cu_8mm.Spe'),
    (10, 'Cu_10mm.Spe'),
    (12, 'Cu_12mm.Spe'),
    (14, 'Cu_14mm.Spe')
]

Pb = [
    (2, 'Pb_2mm.Spe'),
    (2.5, 'Pb_2.5mm.Spe'),
    (3, 'Pb_3mm.Spe'),
    (5, 'Pb_5mm.Spe'),
    (6, 'Pb_6mm.Spe'),
    (9, 'Pb_9mm.Spe')
]

print 'Decays, width'
for (width, filename) in Al:
    y = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            s = str(row[0]).strip()
            if(s.isdigit()):
                y.append(int(s))
    print str(sum(y)) + ', ' + str(width)
