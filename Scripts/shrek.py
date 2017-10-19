import csv
import sys

out_file = open("out.csv", "w")
dic = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stripped = [col.replace('\n', ' ') for col in row]
	#if stripped[2] in dic:
	#	dic[stripped[2]] += 1
	#else:
	#	dic[stripped[2]] = 1	
        out_file.write(str(stripped)[1:len(str(stripped))-1]+ '\n')
#out_file.close()
#maximum = max(dic, key=dic.get)
#print(maximum, dic[maximum])
