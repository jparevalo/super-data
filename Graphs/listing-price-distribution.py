import matplotlib.pyplot as plt
import plotly.plotly as py
import collections
import operator
import sys
import csv

D = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        price = row[9]
        if price != "price":
            if int(price) in D:
                D[int(price)] += 1
            else:
                D[int(price)] = 1

lists = sorted(D.items())
x, y = zip(*lists)

dictionary = plt.figure()

plt.title("Distribution of Listing Prices")
plt.xlabel("Price ($)")
plt.ylabel("# of Listings")
plt.plot(x, y)

plt.savefig(sys.argv[2])
