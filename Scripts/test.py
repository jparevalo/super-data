from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
 
class UsersCount(MRJob):

    def mapper_movie(self, _, line):
        movie_data = line.split(",")
        yield [movie_data[1], movie_data[0]]
 
    def reducer(self, key, values):
	temp_list = [v for v in values]
	yield [key, temp_list]
        #yield ['MAX',[ sum(1 for _ in values), key]]
   
    def mapper_set_users(self,key, value):
	
	if len(value) > 1:
		for value in itertools.combinations(value, 2):
			print value
			yield  [value, 1]
 
    def reducer2(self, key, values):
        yield ['MAX',[sum(values),key]]
	 

    def max_reducer(self, stat, values):
        TEMP = [values]
        yield [stat,max(values)]
 
    def steps(self):
        #return [MRStep(mapper=self.mapper_movie)]
	return [MRStep(mapper=self.mapper_movie, reducer=self.reducer), MRStep(mapper = self.mapper_set_users, reducer = self.reducer2),
           MRStep(reducer=self.max_reducer)]

 
 
if __name__ == '__main__':
    UsersCount.run()
