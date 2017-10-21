from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        calendar_data = line.split(",",3)
	# check if it's aviable
	if calendar_data[2].replace("'",'').strip() != "f" and 'price' not in calendar_data[3] and calendar_data[3].strip().replace("'",'').strip() != '':
		price = calendar_data[3].split("$")[1].strip("'").replace(',','')
        	yield [calendar_data[0].replace("'",''), float(price) ]

    def reducer(self, key, values):
        #values2 = [value for value in values if value != ""]
	#total = float(sum(1 for _ in values))
	suma = 0
	total = 0
	for value in values:
		suma += value
		total += 1

        yield ['AVG',[suma/total ,key]]

    def min_reducer(self, stat, values):
        TEMP = [values]
        yield ['MIN',min(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer),
            MRStep(reducer=self.min_reducer)]


if __name__ == '__main__':
    UsersCount.run()
