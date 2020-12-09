numbers = [int(line.rstrip('\n')) for line in open('data/data.txt')]


def isSum(match, numbers):
    for numberA in numbers:
        for numberB in numbers:
            if numberA + numberB == match:
                return True
    return False


def xmasBreaker(numbers, offset):
    for i in range(offset, len(numbers)):
        candidate = numbers[i]
        if not isSum(candidate, numbers[i - offset:i]):
            return i
    return -1

fault = xmasBreaker(numbers, 25)
print(fault, numbers[fault])
