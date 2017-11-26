
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
from datetime import datetime

class UsersCount(MRJob):
    def mapper_listingid(self, _, line):
        listing_data = line.split(",",3)
        price = listing_data[60].split("$")[1].strip("'").replace(',','')
	rating =listing_data[79]
	listing_id = calendar_data[0].replace("'",'').strip()
	#price 60
	#rating 79
    	yield ["listings", [listing_id,price, rating]]

    def reducer_listings_available_with_total_price(self, listing_id, date_list):
	listing_list = list(date_list)
	
        yield [listing_list[0], [listing_list[1], max(listing_list[2]])]

    def min_reducer(self, stat, values):
        yield ['CHEAPEST AVAILABLE LISTING',min(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_listingid, reducer=self.reducer_dates_by_listing),
                MRStep(reducer=self.reducer_listings_available_with_total_price)]


if __name__ == '__main__':
    UsersCount.run()
