import matplotlib.pyplot as plt
import plotly.plotly as py
import collections
import operator
import sys
import csv

D = {}

text_file_path = sys.argv[1]
txtfile = open(text_file_path, "r")
city = ""
rating = 0
for index, line in enumerate(txtfile):
	if index%2 == 0:
		city = line.strip()
	else:
	    rating = float(line.split()[1])
	D[city] = round(rating,2)

D = collections.OrderedDict(sorted(D.items(), key=operator.itemgetter(1)))


dictionary = plt.figure()

plt.bar(range(len(D)), D.values(), align='center')
plt.title("Average Listing Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
x = range(len(D))
y = D.values()
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.xticks(range(len(D)), D.keys())

plt.savefig(sys.argv[2])
