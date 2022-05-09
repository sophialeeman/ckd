#Read the csv file
import csv
file = open('ckd_clean.csv')
filereader = csv.reader(file)
#Headings
header = []
header = next(filereader)
#Records
rows = []
for row in filereader:
    rows.append(row)
file.close()