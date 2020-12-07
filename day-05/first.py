import math


def calculateRows(position, rowAmmount):
    min = 0
    max = rowAmmount
    for letter in position:
        if letter in 'FL':
            max = min + math.floor((max - min) / 2)
        elif letter in 'BR':
            min = min + math.ceil((max - min) / 2)
    return min


def calculatePosition(sit: str):
    row = calculateRows(sit[:7], 127)
    col = calculateRows(sit[7:], 7)
    return row * 8 + col


sits = [line.rstrip('\n') for line in open('data/data.txt')]

positions = []
for sit in sits:
    positions.append(calculatePosition(sit))

print(max(positions))