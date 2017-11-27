from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv

class UsersCount(MRJob):
    def mapper_userid(self, _, line):
        calendar_data = line.split(",")
        listing_id = calendar_data[0]
        bedrooms = calendar_data[1]
        price = calendar_data[2]
        reviews = calendar_data[3]
        if price != "price" and bedrooms == "1":
            yield ["A", float(price)]

    def reducer(self, key, values):
        yield ['AVG PER LISTING', max(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_userid, reducer=self.reducer)]


if __name__ == '__main__':
    UsersCount.run()
