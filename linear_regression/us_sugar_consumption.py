# Sugar Consumption in the US Diet between 1822 and 2005
#
# Research conducted by: Stephan Guyenet and Jeremy Landen
# Case study prepared by: Robert F. Houser and Georgette Baghdady
#
# Data resource: http://onlinestatbook.com/2/case_studies/sugar.html
# year: All years from 1822 to 2005
# sugar_consum: Estimated consumption of added sugars in the US diet in pounds per year per person
#
# Problem resource: http://wholehealthsource.blogspot.co.id/2012/02/by-2606-us-diet-will-be-100-percent.html


import matplotlib.pyplot as plt
import csv
import numpy as np
from LReg import LReg

# Read dataset
x = list()
y = list()
i = 0
i = 0
with open("us_sugar_consumption.csv") as csvfile:
	cf = csv.reader(csvfile)
	for l in cf:
		if i > 0:
			x.append(int(l[0]))  # year
			y.append(float(l[1]))  # sugar_consum
		else:
			i += 1


# Regression of 1822 - 2005
# i = 0
# j = len(x)
# ls = LReg(x, y)

# Regression of 1822 - 1930
# i = x.index(1822)
# j = x.index(1930) + 1
# ls = LReg(x[i:j], y[i:j])

# Regression of 1931 - 1960
# i = x.index(1931)
# j = x.index(1960) + 1
# ls = LReg(x[i:j], y[i:j])

# Regression of 1961 - 2005
i = x.index(1961)
j = x.index(2005) + 1
ls = LReg(x[i:j], y[i:j])

ls.calculate()
print("correlation = {:.4f}".format(ls.correlation))
print("slope = {:.4f}".format(ls.slope))
print("intercept = {:.4f}".format(ls.intercept))
f = lambda x: ls.slope * x + ls.intercept

# Plot regression line
plt.title('Regression from {0} to {1}'.format(x[i], x[j-1]))
plt.scatter(x, y)
# x = np.array([min(x), max(x)])
plt.axis([1800, 3000, 0, 500])
plt.yticks(range(0, 500, 50))
x = np.array([min(x), 3000])
plt.plot(x, f(x), 'k',
	label="{0:3f} * x + {1:3f}".format(ls.slope, ls.intercept))
plt.ylabel('Sugar Consumption (lb/year/person)')
plt.xlabel('Years')
plt.grid(True)
plt.legend()
plt.show()