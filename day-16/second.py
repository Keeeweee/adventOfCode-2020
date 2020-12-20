def parseIntervals(line: str):
    return [list(map(int, splitted.split('-'))) for splitted in line.split(' or ')]


def isValid(value, constraints):
    for constraint in constraints.values():
        for element in constraint:
            if element[0] <= value <= element[1]:
                return True
    return False


def valuesMatchConstraint(values, constraints):
    for element in values:
        matchesAnyConstraint = False
        for constraint in constraints:
            if (constraint[0] <= element <= constraint[1]):
                matchesAnyConstraint = True
                break
        if not matchesAnyConstraint:
            return False

    return True


def findValidFields(values, constraints):
    validFields = []
    for field, constraint in constraints.items():
        if valuesMatchConstraint(values, constraint):
            validFields.append(field)

    return validFields


myTicketRead = False
otherTicketsRead = False

constraints = {}
myTicket = []
otherTickets = []


for line in open('data/data.txt'):
    value = line.rstrip('\n')
    if value == '':
        continue
    if value == 'your ticket:':
        myTicketRead = True
        otherTicketsRead = False
        continue
    if value == 'nearby tickets:':
        myTicketRead = False
        otherTicketsRead = True
        continue

    if not myTicketRead and not otherTicketsRead:
        label, intervals = value.split(': ')
        constraints[label] = parseIntervals(intervals)

    elif myTicketRead:
        myTicket = list(map(int, value.split(',')))

    else:
        otherTickets.append(list(map(int, value.split(','))))


validTickets = []
for ticket in otherTickets:
    valid = True
    for value in ticket:
        if not isValid(value, constraints):
           valid = False
           break
    if valid:
        validTickets.append(ticket)

fieldValues = list(zip(*validTickets))
fieldMap = []
for values in fieldValues:
    fieldMap.append(set(findValidFields(values, constraints)))

# Future me, I'm sorry if yu are reading the next lines

finalFieldMap = [''] * len(fieldMap)

for i in range(len(fieldMap)):
    lengthOneElement = ''
    index = 0
    for j in range(len(fieldMap)):
        if len(fieldMap[j]) == 1:
            lengthOneElement = list(fieldMap[j])[0]
            index = j
            break
    finalFieldMap[index] = lengthOneElement
    for element in fieldMap:
        try:
            element.remove(lengthOneElement)
        except KeyError:
            continue

departures = []
for i in range(len(finalFieldMap)):
    if 'departure' in finalFieldMap[i]:
        departures.append(i)

total = 1
for departure in departures:
    total *= myTicket[departure]

print(total)