code = [line.rstrip('\n').split(' ') for line in open('data/data.txt')]

for line in code:
    line[1] = int(line[1])


def runCode(code) -> (bool, int):
    currentLine = 0
    visitedLines = []
    count = 0
    while currentLine not in visitedLines and currentLine < len(code):
        visitedLines.append(currentLine)
        instruction, value = code[currentLine]
        if instruction == 'acc':
            count += value
            currentLine += 1
        elif instruction == 'jmp':
            currentLine += value
        elif instruction == 'nop':
            currentLine += 1
    return currentLine >= len(code), count


for line in code:
    instruction, value = line
    if instruction == 'jmp':
        line[0] = 'nop'
        result = runCode(code)
        line[0] = 'jmp'
    elif instruction == 'nop':
        line[0] = 'jmp'
        result = runCode(code)
        line[0] = 'nop'
    else:
        continue
    if result[0]:
        print(result[1])
        break