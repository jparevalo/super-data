from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        #listing_data =  csv.reader(line)
        rating_data = line.split(",")
        # check if it's aviable
       	print rating_data 
        if rating_data[0] != "listing_id":
                yield [rating_data[0], 1 ]

    def reducer(self, key, values):
        yield ['MAX',[sum(values), key]]

    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat,max(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer),
            MRStep(reducer=self.max_reducer)]


if __name__ == '__main__':
    UsersCount.run()
