lines = [line.rstrip('\n').split(': ') for line in open('data/data.txt')]

def passwordIsValid(condition: str, password: str) -> bool:
    ammount, letter = condition.split(' ')
    min, max = ammount.split('-')
    return int(min) <= password.count(letter) <= int(max)

count = 0
for line in lines:
    if passwordIsValid(line[0], line[1]):
        count += 1

print(count)
