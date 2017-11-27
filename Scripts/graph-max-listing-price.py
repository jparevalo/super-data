import matplotlib.pyplot as plt
import plotly.plotly as py
import collections
import operator
import sys
import csv

D = {}
prices = {"AMSTERDAM":1.17825, "DUBLIN":1.17825, "HONG KONG":0.128144, "NEW YORK":1, "MADRID":1.17825, "PARIS":1.17825} # Euro, Euro, HKD, USD, Euro, Euro

text_file_path = sys.argv[1]
txtfile = open(text_file_path, "r")
city = ""
price = 0
for index, line in enumerate(txtfile):
	if index%2 == 0:
		city = line.strip()
	else:
	    price = prices[city] * float(line.split()[3])
	D[city] = round(price,2)

D = collections.OrderedDict(sorted(D.items(), key=operator.itemgetter(1)))


dictionary = plt.figure()

plt.bar(range(len(D)), D.values(), align='center')
plt.title("Max Listing Price (Same Currency)")
plt.xlabel("City")
plt.ylabel("Average Price (US$)")
x = range(len(D))
y = D.values()
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.xticks(range(len(D)), D.keys())

plt.savefig(sys.argv[2])
