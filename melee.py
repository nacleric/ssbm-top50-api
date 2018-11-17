import csv

def print_player(player):
    matchup_data = []
    json = {}
    csvFile = open('2018h2h.csv')
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader) 

    csvData[0] = list(filter(None, csvData[0]))     #filters all the empty strings
    opponents = csvData[0]                          #csvData[0] changed to opponents for readability
    for row in csvData[1:]:                         
        if player in row:                           
            for col in row:
                matchup_data.append(col)            #puts all values into matchup_data
    counter = 0                                     
    for i in range(1,len(matchup_data),2):
        if matchup_data[i] == '':                   #turns empty string to 0's
            matchup_data[i] = '0'
            matchup_data[i+1] = '0'
        json[str(opponents[counter])] = {'wins': matchup_data[i],'losses': matchup_data[i+1]}
        counter += 1
    return json
    csvFile.close()

'''
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


