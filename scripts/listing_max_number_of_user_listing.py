from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
	listing_data =  csv.reader(line)
        #listing_data = line.split(",")
	host_id_idx = 19
        # check if it's aviable
	print listing_data
        if listing_data[host_id_idx] != "host_id":
                yield [listing_data[host_id_idx], 1 ]

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


