import math


def degToRad(degrees):
    return degrees * 2 * math.pi / 360


instructions = [(line.rstrip('\n')[0], int(line.rstrip('\n')[1:])) for line in open('data/data.txt')]

xWaypoint = 10
yWaypoint = 1
degrees = 0
xShip = 0
yShip = 0
for instruction in instructions:
    if instruction[0] == 'N':
        yWaypoint += instruction[1]
    elif instruction[0] == 'S':
        yWaypoint -= instruction[1]
    elif instruction[0] == 'E':
        xWaypoint += instruction[1]
    elif instruction[0] == 'W':
        xWaypoint -= instruction[1]
    elif instruction[0] in 'RL':
        diffX = xWaypoint - xShip
        diffY = yWaypoint - yShip
        radAngle = degToRad(instruction[1])
        if instruction[0] == 'R':
            radAngle *= -1

        x2 = int(diffX * math.cos(radAngle)) - int(diffY * math.sin(radAngle))
        y2 = int(diffX * math.sin(radAngle)) + int(diffY * math.cos(radAngle))
        xWaypoint = x2 + xShip
        yWaypoint = y2 + yShip

    elif instruction[0] == 'F':
        moveX = int(instruction[1] * (xWaypoint - xShip))
        moveY = int(instruction[1] * (yWaypoint - yShip))
        xShip += moveX
        xWaypoint += moveX
        yShip += moveY
        yWaypoint += moveY

    # print(instruction)
    # print('Ship:', xShip, yShip)
    # print('Waypoint:', xWaypoint, yWaypoint)

print(abs(xShip) + abs(yShip))