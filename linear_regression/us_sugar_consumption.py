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
			x.append(float(l[0]))  # year
			y.append(float(l[1]))  # sugar_consum
		else:
			i += 1


# Find regression function
ls = LReg(x, y)
print("correlation = {:.2f}".format(ls.correlation))
print("slope = {:.2f}".format(ls.slope))
print("intercept = {:.2f}".format(ls.intercept))
f = lambda x: ls.slope * x + ls.intercept