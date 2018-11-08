import fileinput

for line in fileinput.input("2018h2h.csv", inplace=1):
    print(line.lower(), end='')
