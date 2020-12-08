class Bag:
    def __init__(self, key: str, contains):
        self.color = key.replace('bags', '').strip()
        self.contains = {}
        for bag in contains:
            bag = bag[:-4] if bag[-1] == 's' else bag[:-3]
            bag = bag.strip()
            ammount = int(bag[0])
            color = bag[2:]
            self.contains[color] = ammount

    def __str__(self):
        return self.color + ' contains ' + str(self.contains.keys())


def findContainers(key, rules):
    containers = []
    for rule in rules:
        if key in rules[rule].contains:
            containers.append(rule)
    return containers


def ruleFinder(key, rules, containerBags: set):
    containers = findContainers(key, rules)
    for container in containers:
        containerBags.add(container)
        ruleFinder(container, rules, containerBags)


rawRules = [line.rstrip('\n') for line in open('data/data.txt')]

rules = {}
for rule in rawRules:
    key, value = rule.replace('.', '').split(' contain ')
    key = key[:-4] if key[-1] == 's' else key[:-3]
    rules[key.strip()] = Bag(key.strip(), [] if value == 'no other bags' else value.split(', '))

containerBags = set()
ruleFinder('shiny gold', rules, containerBags)

print(len(containerBags))