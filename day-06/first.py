batch = [line.rstrip('\n') for line in open('data/data.txt')]

answerLine = ''
groups = []
for line in batch:
    if line == '':
        groups.append(set(answerLine.replace(' ', '')))
        answerLine = ''
        continue

    answerLine += line
groups.append(set(answerLine.replace(' ', '')))


print(sum(map(len, groups)))
