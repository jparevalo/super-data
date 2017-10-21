from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_listingid(self, _, line):
        calendar_data = line.split(",",3)
    	# check if it's aviable
    	if calendar_data[2].replace("'",'').strip() == "f":
    	    yield [calendar_data[0].replace("'",''), 1 ]

    def reducer(self, key, values):
	       yield ['MAX',[sum(values), key]]

    def max_reducer(self, stat, values):
        yield [stat,max(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_listingid, reducer=self.reducer),
            MRStep(reducer=self.max_reducer)]


if __name__ == '__main__':
    UsersCount.run()
