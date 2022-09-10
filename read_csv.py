import csv

with open('fake_data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)

    for row in myreader:
        print(row['lat'])