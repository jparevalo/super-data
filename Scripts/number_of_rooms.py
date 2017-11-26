from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
 
class UsersCount(MRJob):

    def mapper_movie(self, _, line):
        listing_data = line.split(",")
        yield [listing_data[1], 1]
 
    def reducer(self, number_of_rooms, values):
	yield [number_of_rooms, sum(values)]
 
    def reducer2(self, key, values):
        yield ['MAX',[sum(values),key]]
	 
    def steps(self):
        #return [MRStep(mapper=self.mapper_movie)]
	return [MRStep(mapper=self.mapper_movie, reducer=self.reducer)]

 
 
if __name__ == '__main__':
    UsersCount.run()
