instructions = [line.rstrip('\n').split(' = ') for line in open('data/data.txt')]


def calculateMaskedValue(memVal: str, mask):
    value = list(memVal)

    for i in range(len(mask)):
        maskBit = mask[i]
        if maskBit != '0':
            value[i] = mask[i]
    return value


def getMemoryPositions(maskedPositions, index,  memPositions):
    if index == len(maskedPositions):
        memPositions.append(int(''.join(maskedPositions), 2))
        return
    if maskedPositions[index] == 'X':
        getMemoryPositions(maskedPositions[:index] + ['0'] + maskedPositions[index + 1:], index + 1, memPositions)
        getMemoryPositions(maskedPositions[:index] + ['1'] + maskedPositions[index + 1:], index + 1, memPositions)
    else:
        getMemoryPositions(maskedPositions, index + 1, memPositions)
    return


mask = []
memory = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        mask = list(instruction[1])
        continue

    instruction[0] = instruction[0].replace('mem[', '')
    instruction[0] = instruction[0].replace(']', '')
    memoryPos = "{0:b}".format(int(instruction[0]))
    memoryPos = (36 - len(memoryPos)) * '0' + memoryPos
    value = int(instruction[1])

    maskedMemPositions = calculateMaskedValue(memoryPos, mask)
    memoryPositions = []

    getMemoryPositions(maskedMemPositions, 0, memoryPositions)

    for memoryPosition in memoryPositions:
        memory[memoryPosition] = value

print(sum(memory.values()))