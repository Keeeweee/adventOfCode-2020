lines = [line.rstrip('\n').split(': ') for line in open('data/data.txt')]

def passwordIsValid(condition: str, password: str) -> bool:
    ammount, letter = condition.split(' ')
    min, max = ammount.split('-')
    return (password[int(min) - 1] == letter) != (password[int(max) - 1] == letter)

count = 0
for line in lines:
    if passwordIsValid(line[0], line[1]):
        count += 1

print(count)
