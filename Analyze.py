#Read the csv file
import csv
file = open('ckd_clean.csv')
filereader = csv.reader(file)
header = []
header = next(filereader)
