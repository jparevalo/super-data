from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
 
class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        listing_data = line.split(",")
	l_id = listing_data[0]
	try:
	    l_price = int(listing_data[9])
	    yield [l_id, l_price]
	except:
	    print "[ Error formating ]"
 
    def reducer(self, key, values):
        yield ['MAX',[sum(values),key]]
 
    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat,max(values)]
 
    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer),
            MRStep(reducer=self.max_reducer)]
 
 
if __name__ == '__main__':
    UsersCount.run()
