with open('data/test_01.txt') as data:
    calledNumbers = list(map(int, data.readline().split(',')))

turn = len(calledNumbers)

while turn < 2020:
    try:
        index = len(calledNumbers) - calledNumbers[-2::-1].index(calledNumbers[-1]) - 1
    except ValueError:
        calledNumbers.append(0)
        turn += 1
        continue

    calledNumbers.append(turn - index)
    turn += 1

print(calledNumbers[-1])