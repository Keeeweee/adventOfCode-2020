numbers = [int(line.rstrip('\n')) for line in open('data/test_01.txt')]

numbers.append(0)
numbers.append(max(numbers) + 3)
numbers = sorted(numbers)

diffOne = 0
diffTwo = 0
diffThree = 0
for i in range(len(numbers) - 1):
    number = numbers[i]
    nextNumber = numbers[i+1]
    diff = nextNumber - number
    if diff > 3:
        break
    elif diff == 3:
        diffThree += 1
    elif diff == 2:
        diffTwo += 1
    elif diff == 1:
        diffOne += 1

print(diffOne, diffThree)
print(diffOne * (diffThree))
