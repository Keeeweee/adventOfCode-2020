with open('data/data.txt') as data:
    myArrival = int(data.readline())
    busIds = [int(id) if id != 'x' else None for id in data.readline().split(',')]


def checkDepartures(t, busIds):
    for i in range(len(busIds)):
        id = busIds[i]
        if id is None:
            continue

        if (t + i) % id != 0:
            return False
    return True


t = 100000000000000
while not checkDepartures(t, busIds):
    if t % 1000000 == 0:
        print(t)
    t += 1


print(t)