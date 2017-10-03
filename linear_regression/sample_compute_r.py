import math
from sample_data import *

# Number of rows, let assumed that length of X and Y always equal
n = len(x)

# r = (sum(XY) - ( (sum(X) * sum(Y))/N ))/( sqrt( sum(X^2) - (sum(X)^2 / N) ) * sqrt( sum(Y^2) - (sum(Y)^2 / N) ) )
sx = 0
for i in x:
	sx += i
sy = 0
for i in y:
	sy += i
a = (sx*sy) / n
r = 0
for i in range(0, n):
	r += x[i]*y[i]
r = r - a
a = 0
for i in x:
	a += (i*i)
a = a - ((sx*sx)/n)
a = math.sqrt(a)
b = 0
for i in y:
	b += (i*i)
b = b - ((sy*sy)/n)
b = math.sqrt(b)
a = a*b
r = r/a