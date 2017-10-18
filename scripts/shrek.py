import csv
import sys
import operator

out_file = open("out.csv", "w")
dic = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stripped = [col.replace('\n', ' ') for col in row]
	if stripped[0] in dic:
		dic[stripped[0]] += 1
	else:
		dic[stripped[0]] = 1	
        out_file.write(str(stripped)[1:len(str(stripped))-1]+ '\n')
out_file.close()
print dic
