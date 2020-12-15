with open('data/data.txt') as data:
    initialNumbers = list(map(int, data.readline().split(',')))

turn = 0
calledNumbers = {}
lastNumber = 0
for number in initialNumbers[:-1]:
    turn += 1
    calledNumbers[number] = [turn, False]

lastNumber = initialNumbers[-1]

while turn < 30000000 - 1:
    turn += 1
    if turn % 1000000 == 0: print('Current turn: ', turn)
    if lastNumber not in calledNumbers.keys():
        calledNumbers[lastNumber] = [turn, False]
        lastNumber = 0
    else:
        element = calledNumbers[lastNumber]
        calledNumbers[lastNumber] = [turn, False]
        lastNumber = turn - element[0]

print(lastNumber)