with open('data/data.txt') as data:
    myArrival = int(data.readline())
    busIds = data.readline().split(',')

minutesUntilDeparture = []
for id in busIds:
    if id == 'x':
        minutesUntilDeparture.append(myArrival + 1)
    else:
        minutesUntilDeparture.append(int(id) - (myArrival % int(id)))

minMinutes = min(minutesUntilDeparture)
minPosition = minutesUntilDeparture.index(minMinutes)
minId = int(busIds[minPosition])
print(minMinutes * minId)