from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
 
class UsersCount(MRJob):

    def mapper_movie(self, _, line):
        listing_data = line.split(",")
	if listing_data[4] != "":
	    try:
		yield ["cal", float(listing_data[4])]
	    except:
		pass
 
    def reducer(self, key, values):
	suma = 0
	total = 0
	for value in values:
	    suma += value
	    total +=1
	    
	yield ["Avg1", ((suma / total)/10) * 5]

	 
    def steps(self):
        #return [MRStep(mapper=self.mapper_movie)]
	return [MRStep(mapper=self.mapper_movie, reducer=self.reducer)]

 
 
if __name__ == '__main__':
    UsersCount.run()
