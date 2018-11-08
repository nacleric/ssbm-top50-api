import csv
#import json

#player=input('select player: ')

def print_player(player):
    foo = []
    csvFile = open('2018h2h.csv')
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader) 
    csvData[0] = list(filter(None, csvData[0]))     #filters all the empty strings
    for row in csvData[1:]:                             #iterates threw each row of csvData
        if player in row:                           #finds the selected player and prints out info
            for col in row:
                #print(col,end='')
                foo.append(col)
            print('\n')
    return str(foo)
    csvFile.close()

def print_all():    #prints out all rows 
    csvFile = open('2018h2h.csv')
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader) 
    csvData[0] = list(filter(None, csvData[0]))     #filters all the empty strings
    count=0  
    for row in csvData:
        count+=1
        print('row:',count)
        for col in row:
            print(col, end='')
        print('\n')




'''
data = list(csvReader)

player = data[1][2]
opponent = data[0][5]
wins = data[1][5]
losses = data[1][6]

print(player,' is ',wins, '-',losses,' against ',opponent)
'''
'''
with open('2018top50h2h.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print('Row #' + str(reader.line_num) + ' ' + str(row))
'''
