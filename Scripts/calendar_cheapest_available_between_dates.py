from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re
import itertools
import csv
from datetime import datetime

START_DATE = datetime.strptime("2017-11-07", "%Y-%m-%d")
END_DATE = datetime.strptime("2017-11-14", "%Y-%m-%d")
class UsersCount(MRJob):
    def mapper_listingid(self, _, line):
        calendar_data = line.split(",",3)
    	# check if it's aviable
    	if calendar_data[2].replace("'",'').strip() != "f" and calendar_data[1].replace("'",'').strip() != "date":
            price = calendar_data[3].split("$")[1].strip("'").replace(',','')
            rent_date = datetime.strptime(calendar_data[1].replace("'",'').strip(), "%Y-%m-%d")
            if START_DATE <= rent_date <= END_DATE:
    	           yield [calendar_data[0].replace("'",'').strip(), [price,calendar_data[1].replace("'",'').strip()]]

    def reducer_dates_by_listing(self, listing_id, date_available):
        yield listing_id, list(date_available)

    def reducer_listings_available_with_total_price(self, listing_id, date_list):
        for dates in date_list:
            if len(dates) == (END_DATE - START_DATE).days + 1:
            	total = 0
                for date in dates:  # dates = [[price1, date1], ...]
                    total += float(date[0])
                    yield ['TOTAL PRICE',[total ,listing_id]]

    def min_reducer(self, stat, values):
        yield ['CHEAPEST AVAILABLE LISTING',min(values)]

    def steps(self):
        return [MRStep(mapper=self.mapper_listingid, reducer=self.reducer_dates_by_listing),
                MRStep(reducer=self.reducer_listings_available_with_total_price),
                MRStep(reducer=self.min_reducer)]


if __name__ == '__main__':
    UsersCount.run()
