import csv


output = open("myCsv.csv", mode = 'w') # opening file in write mode
mywriter = csv.writer(output)
header = ['name', 'age']
mywriter.writerow(header)
data = ['Bob Smith', 40]
mywriter.writerow(data)
output.close()