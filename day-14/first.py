instructions = [line.rstrip('\n').split(' = ') for line in open('data/data.txt')]


def calculateMemValue(value: str, mask):
    value = list(value)

    for i in range(len(mask)):
        maskBit = mask[i]
        if maskBit != 'X':
            value[i] = mask[i]
    return int(''.join(value), 2)

mask = []
memory = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        mask = list(instruction[1])
        continue

    instruction[0] = instruction[0].replace('mem[', '')
    instruction[0] = instruction[0].replace(']', '')
    memoryPos = int(instruction[0])
    value = "{0:b}".format(int(instruction[1]))
    value = (36 - len(value)) * '0' + value

    memory[memoryPos] = calculateMemValue(value, mask)

print(sum(memory.values()))