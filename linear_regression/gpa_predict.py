# We will used linear regression to find relation between SAT score and GPA.
# Our prediction is not based on assumption, but purely statistic.
# Correlation between fact, that is SAT score achieved student at high school
# and determined result, that is GPA which will be achieve when student in university.
# References: http://onlinestatbook.com/2/case_studies/sat.html
# Data: sat.csv
# 	high_GPA	High school grade point average
# 	math_SAT	Math SAT score
# 	verb_SAT	Verbal SAT score
# 	comp_GPA	Computer science grade point average
# 	univ_GPA	Overall university grade point average
# The scatter plot between high_GPA and univ_GPA coded in gpa_plot.py

import matplotlib.pyplot as plt
import csv
import numpy as np
from LReg import LReg

# Read dataset
x = list()
y = list()
i = 0
i = 0
with open("gpa_sat.csv") as csvfile:
	cf = csv.reader(csvfile)
	for l in cf:
		if i > 0:
			x.append(float(l[0]))  # high_GPA
			y.append(float(l[4]))  # Univ_GPA
		else:
			i += 1

# Find regression function
ls = LReg(x, y)
print("correlation = {:.2f}".format(ls.correlation))
print("slope = {:.2f}".format(ls.slope))
print("intercept = {:.2f}".format(ls.intercept))
f = lambda x: ls.slope * x + ls.intercept

# Predict if someone has 2.2 GPA in High School
print("2.2 GPA at high school -> {:.2f} GPA at university".format(f(2.2)))

# Predict if someone has 3.0 GPA in High School
print("3.0 GPA at high school -> {:.2f} GPA at university".format(f(3.0)))

# Predict if someone has 4.0 GPA in High School
print("4.0 GPA at high school -> {:.2f} GPA at university".format(f(4.0)))

# Plot regression line
plt.scatter(x, y)
x = np.array([min(x), max(x)])
plt.plot(x, f(x), label='Regression line')
plt.ylabel('University GPA')
plt.xlabel('High School GPA')
plt.legend()
plt.show()