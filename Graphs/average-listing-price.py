import matplotlib.pyplot as plt
import plotly.plotly as py
import collections
import operator
import sys
import csv

D = {}
prices = [1.17825, 1.17825, 1.17825, 0.128144, 1] #Euro, Euro, Euro, HKD, USD
total = int(sys.argv[1])
for i in range(total):
    total_sum = 0
    n = 0
    with open(sys.argv[2+i]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            price = row[9]
            if price != "price":
                total_sum += int(price)*prices[i]
                n += 1
        D[sys.argv[2+i].split('/')[2]] = int(round(total_sum/n))

D = collections.OrderedDict(sorted(D.items(), key=operator.itemgetter(1)))


dictionary = plt.figure()

plt.bar(range(len(D)), D.values(), align='center')
plt.title("Average Listing Price (Same Currency)")
plt.xlabel("City")
plt.ylabel("Average Price (US$)")
x = range(len(D))
y = D.values()
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.xticks(range(len(D)), D.keys())

plt.savefig(sys.argv[2+total])
