batch = [line.rstrip('\n') for line in open('data/data.txt')]

groups = []
group = set()
first = True
for line in batch:
    if line == '':
        groups.append(group)
        group = set()
        first = True
        continue
    if first:
        group = set(line.replace(' ', ''))
        first = False
    else:
        group = group.intersection(set(line.replace(' ', '')))

groups.append(group)

print(sum(map(len, groups)))
