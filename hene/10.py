from math import *

d = 0.496
R = 0.51
c = 3.0e8

v = c / (2*d) * (2 + 2*acos(1-d/R)/pi)

print v
