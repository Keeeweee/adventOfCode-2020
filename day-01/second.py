match = 2020


def findMatch(numbers):
    for number in numbers:
        for otherNumber in numbers:
            for otherOtherNumber in numbers:
                if number + otherNumber + otherOtherNumber == match:
                    return number, otherNumber, otherOtherNumber


numbers = [int(line.rstrip('\n')) for line in open('data/data.txt')]

keys = findMatch(numbers)
print(keys[0] * keys[1] * keys[2])