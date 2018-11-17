import csv
#import json


def print_player(player):
    matchup_data = []
    #json = {player:{wins:5,losses:5},}
    csvFile = open('2018h2h.csv')
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader) 

    #csvData[0] is the list of players because it is the first row in the csv sheet
    csvData[0] = list(filter(None, csvData[0]))     #filters all the empty strings
    opponents = csvData[0]
    for row in csvData[1:]:                         #iterates threw each row of csvData
        if player in row:                           #finds the selected player and prints out info
            for col in row:
                matchup_data.append(col) #puts all values into matchup_data
    counter = 0 #counter is needed to iterate through the list of players
    for i in range(1,len(matchup_data),2):
        if matchup_data[i] == '': #turns empty string to 0's
            matchup_data[i] = '0'
            matchup_data[i+1] = '0'
        #json[str(csvData[0][counter])][]
        print(opponents[counter],':','wins-',matchup_data[i],'losses-',matchup_data[i+1])
        counter+=1
    return str(matchup_data)
    csvFile.close()


def print_all():                                    #prints out all rows 
    csvFile = open('2018h2h.csv')
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader) 
    csvData[0] = list(filter(None, csvData[0]))     #filters all the empty strings
    counter=0  
    for row in csvData:
        counter+=1
        print('row:',counter)
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
