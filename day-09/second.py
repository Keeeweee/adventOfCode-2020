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

def xmasContiguousFinder(match, numbers):
    for i in range(len(numbers)-1):
        count = numbers[i]
        for j in range(i+1, len(numbers)):
            if count == match:
                return numbers[i:j]
            if count > match:
                break
            else:
                count += numbers[j]
    return None

fault = xmasBreaker(numbers, 25)

solution = xmasContiguousFinder(numbers[fault], numbers)

print(min(solution) + max(solution))

