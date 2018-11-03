import csv

csvFile = open('2018h2h.csv')
lower_stream = (line.lower() for line in csvFile)
csv_reader = csv.reader(lower_stream, delimiter=' ', quotechar='"', escapechar='^')
