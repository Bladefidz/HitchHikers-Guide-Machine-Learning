import csv

# Get sample
x = list()
y = list()
i = 0
with open("sample.csv") as csvfile:
	cf = csv.reader(csvfile)
	for l in cf:
		if i > 0:
			x.append(int(l[0]))
			y.append(int(l[1]))
		else:
			i += 1