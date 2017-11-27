import matplotlib.pyplot as plt
import plotly.plotly as py
import collections
import operator
import sys
import csv

D = {}
days_per_review = 7
months_per_year = 12
text_file_path = sys.argv[1]
txtfile = open(text_file_path, "r")
city = ""
days_rented_per_year = 0
for index, line in enumerate(txtfile):
	if index%2 == 0:
		city = line.strip()
	else:
	    days_rented_per_year = days_per_review * months_per_year * float(line.split()[2])
	D[city] = int(round(days_rented_per_year))

D = collections.OrderedDict(sorted(D.items(), key=operator.itemgetter(1)))


dictionary = plt.figure()

plt.bar(range(len(D)), D.values(), align='center')
plt.title("Average Rents per Year")
plt.xlabel("City")
plt.ylabel("Times Rented")
x = range(len(D))
y = D.values()
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.xticks(range(len(D)), D.keys())

plt.savefig(sys.argv[2])
