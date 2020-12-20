import copy

initialGrid = [list(line.rstrip('\n')) for line in open('data/data.txt')]

CYCLES = 6
X = len(initialGrid[0])
Y = len(initialGrid)

MAX_X = X + CYCLES * 2
MAX_Y = Y + CYCLES * 2
MAX_Z = CYCLES * 2 + 1


def printGrid(grid):
    for level in grid:
        for row in level:
            print(row)
        print()


def getEmptyGrid(x, y, cycles):
    newGrid = []
    for i in range(y + cycles * 2):
        newGrid.append(['.'] * (x + cycles * 2))
    return newGrid


def getNeighbours(x, y, z):
    neighbours = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if 0 <= i < MAX_X and 0 <= j < MAX_Y and 0 <= k < MAX_Z:
                    if not (i == x and j == y and k == z):
                        neighbours.append([k, j, i])
    return neighbours


def getInactiveNeighbours(grid, neighbours):
    count = 0
    for neighbour in neighbours:
        if grid[neighbour[0]][neighbour[1]][neighbour[2]] == '.':
            count += 1
    return count


def getActiveNeighbours(grid, neighbours):
    count = 0
    for neighbour in neighbours:
        if grid[neighbour[0]][neighbour[1]][neighbour[2]] == '#':
            count += 1
    return count


def runCycle(grid):
    newTurnGrid = copy.deepcopy(grid)

    for level in range(len(grid)):
        for row in range(len(grid[level])):
            for col in range(len(grid[level][row])):
                neighbours = getNeighbours(col, row, level)
                activeNeighbours = getActiveNeighbours(grid, neighbours)
                if grid[level][row][col] == '#':
                    if not (2 <= activeNeighbours <= 3):
                        newTurnGrid[level][row][col] = '.'
                else:
                    if activeNeighbours == 3:
                        newTurnGrid[level][row][col] = '#'

    return newTurnGrid



grid = []
for i in range(2 * CYCLES + 1):
    grid.append(getEmptyGrid(X, Y, CYCLES))


for i in range(X):
    for j in range(Y):
        grid[CYCLES][i + CYCLES][j + CYCLES] = initialGrid[i][j]

for i in range(CYCLES):
    grid = runCycle(grid)

total = 0
for level in range(len(grid)):
    for row in range(len(grid[level])):
        for col in range(len(grid[level][row])):
            if grid[level][row][col] == '#':
                total += 1

print(total)
