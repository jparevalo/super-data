import csv
import sys

out_file = open(sys.argv[2], "w")
dic = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stripped = [col.replace('\n', ' ') for col in row]	
        out_file.write(str(stripped)[1:len(str(stripped))-1]+ '\n')
out_file.close()

