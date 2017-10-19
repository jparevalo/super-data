from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        calendar_data = line.split(",")
	# check if it's aviable
	if calendar_data[2].strip("'") != "f" and 'price' not in calendar_data[3] and calendar_data[3].strip().strip("'") != '':
		price = calendar_data[3].split("$")[1].strip("'")
        	yield [calendar_data[0].strip("'"), float(price) ]

    def reducer(self, key, values):
        #values2 = [value for value in values if value != ""]
	#total = float(sum(1 for _ in values)) 
	suma = 0
	total = 0
	for value in values:
		suma += value
		total += 1
	
        yield ['AVG',[suma/total ,key]]

    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat,max(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer),
            MRStep(reducer=self.max_reducer)]


if __name__ == '__main__':
    UsersCount.run()

