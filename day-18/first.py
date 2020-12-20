operations = [list(line.rstrip('\n').replace(' ', '')) for line in open('data/data.txt')]
print(operations)

def calculate(operation):
    prevPos = 0
    index = 0
    if (operation[0] == '('):
        total, newIndex = calculate(operation[1:])
        index += newIndex
    else:
        total = int(operation[0])
    while index < len(operation) - 1:
        index += 1
        el = operation[index]
        if el not in '+*()':
            if prevPos == '+':
                total += int(el)
            elif prevPos == '*':
                total *= int(el)
            continue

        if el in '+*':
            prevPos = el

        if el == ')':
            return total, index + 1

        if el == '(':
            result, newIndex = calculate(operation[index+1:])
            index += newIndex
            if prevPos == '+':
                total += result
            elif prevPos == '*':
                total *= result
            continue

    return total, len(operation)

total = 0
for operation in operations:
    total += calculate(operation)[0]

print(total)