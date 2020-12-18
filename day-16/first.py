def parseIntervals(line: str):
    return [list(map(int, splitted.split('-'))) for splitted in line.split(' or ')]


def isValid(value, constraints):
    for constraint in constraints.values():
        for element in constraint:
            if element[0] <= value <= element[1]:
                return True
    return False


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
        myTicket = map(int, value.split(','))

    else:
        otherTickets.append(map(int, value.split(',')))


errors = []
for ticket in otherTickets:
    for value in ticket:
        if not isValid(value, constraints):
            errors.append(value)

print(sum(errors))