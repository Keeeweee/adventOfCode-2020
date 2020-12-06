map = [line.rstrip('\n') for line in open('data/data.txt')]


TREE = '#'
count = 0
step = 1
offset = 0
for row in range(0, len(map), step):
    if map[row][offset % len(map[row])] == TREE:
        count += 1
    offset += 3

print(count)