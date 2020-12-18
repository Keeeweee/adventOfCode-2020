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


for line in open('data/test_02.txt'):
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
        myTicket = map(int, value.split(','))

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
    fieldMap.append(findValidFields(values, constraints))


print(fieldMap)
print(fieldValues)