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
        date = row[1]
        if date != "date":
            if date in D:
                D[date] += 1
            else:
                D[date] = 1

lists = sorted(D.items())
x, y = zip(*lists)

dictionary = plt.figure()
plt.bar(range(len(D)), D.values(), align='center')
plt.title("Listings per day")
plt.xlabel("Day")
plt.ylabel("# Listings")
x = range(len(D))
y = D.values()

plt.savefig(sys.argv[2])
