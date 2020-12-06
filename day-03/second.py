map = [line.rstrip('\n') for line in open('data/data.txt')]


def treeHitCalculator(map, offset: int, step: int):
    TREE = '#'
    count = 0
    x = 0
    for row in range(0, len(map), step):
        if map[row][x % len(map[row])] == TREE:
            count += 1
        x += offset
    return count


combinations = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

total = 1
for combination in combinations:
    total *= treeHitCalculator(map, combination[0], combination[1])

print(total)
