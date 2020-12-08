code = [line.rstrip('\n').split(' ') for line in open('data/data.txt')]

for line in code:
    line[1] = int(line[1])

currentLine = 0
visitedLines = []
count = 0
while currentLine not in visitedLines:
    visitedLines.append(currentLine)
    instruction, value = code[currentLine]
    if instruction == 'acc':
        count += value
        currentLine += 1
    elif instruction == 'jmp':
        currentLine += value
    elif instruction == 'nop':
        currentLine += 1

print(count)