import math

instructions = [(line.rstrip('\n')[0], int(line.rstrip('\n')[1:])) for line in open('data/data.txt')]

x = 0
y = 0
degrees = 0
for instruction in instructions:
    if instruction[0] == 'N':
        y += instruction[1]
    elif instruction[0] == 'S':
        y -= instruction[1]
    elif instruction[0] == 'E':
        x += instruction[1]
    elif instruction[0] == 'W':
        x -= instruction[1]
    elif instruction[0] == 'L':
        degrees += instruction[1]
    elif instruction[0] == 'R':
        degrees -= instruction[1]
    elif instruction[0] == 'F':
        x += int(instruction[1] * math.cos(degrees * 2 * math.pi / 360))
        y += int(instruction[1] * math.sin(degrees * 2 * math.pi / 360))

print(x, y)
print(abs(x) + abs(y))