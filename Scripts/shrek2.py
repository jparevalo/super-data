import csv
import sys

out_file = open(sys.argv[2], "w")
dic = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
	_id = row[0]
	_rooms = row[55]
	_price = row[60].replace("$","")
	_number_of_rev = row[76]
	col = _id+","+_rooms+","+_price+","+_number_of_rev
        #stripped = [col.replace('\n', ' ') for col in row]	
        out_file.write(col +'\n' )
out_file.close()

