import copy

initialGrid = [list(line.rstrip('\n')) for line in open('data/data.txt')]

CYCLES = 6
X = len(initialGrid[0])
Y = len(initialGrid)

MAX_X = X + CYCLES * 2
MAX_Y = Y + CYCLES * 2
MAX_Z = CYCLES * 2 + 1
MAX_A = CYCLES * 2 + 1


def printGrid(grid):
    for metalevel in grid:
        for level in metalevel:
            for row in level:
                print(row)
            print()
        print()


def getEmptyGrid(x, y, cycles):
    newGrid = []
    for i in range(y + cycles * 2):
        newGrid.append(['.'] * (x + cycles * 2))
    return newGrid


def getNeighbours(x, y, z, a):
    neighbours = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(a - 1, a + 2):
                    if 0 <= i < MAX_X and 0 <= j < MAX_Y and 0 <= k < MAX_Z and 0 <= l < MAX_A:
                        if not (i == x and j == y and k == z and l == a):
                            neighbours.append([l, k, j, i])
    return neighbours


def getInactiveNeighbours(grid, neighbours):
    count = 0
    for neighbour in neighbours:
        if grid[neighbour[0]][neighbour[1]][neighbour[2]][neighbour[3]] == '.':
            count += 1
    return count


def getActiveNeighbours(grid, neighbours):
    count = 0
    for neighbour in neighbours:
        if grid[neighbour[0]][neighbour[1]][neighbour[2]][neighbour[3]] == '#':
            count += 1
    return count


def runCycle(grid):
    newTurnGrid = copy.deepcopy(grid)

    for metalevel in range(len(grid)):
        for level in range(len(grid[metalevel])):
            for row in range(len(grid[metalevel][level])):
                for col in range(len(grid[metalevel][level][row])):
                    neighbours = getNeighbours(col, row, level, metalevel)
                    activeNeighbours = getActiveNeighbours(grid, neighbours)
                    if grid[metalevel][level][row][col] == '#':
                        if not (2 <= activeNeighbours <= 3):
                            newTurnGrid[metalevel][level][row][col] = '.'
                    else:
                        if activeNeighbours == 3:
                            newTurnGrid[metalevel][level][row][col] = '#'

    return newTurnGrid



grid = []
for i in range(2 * CYCLES + 1):
        grid.append(getEmptyGrid(X, Y, CYCLES))

metagrid = []
for i in range(2 * CYCLES + 1):
        metagrid.append(copy.deepcopy(grid))

for i in range(X):
    for j in range(Y):
        metagrid[CYCLES][CYCLES][i + CYCLES][j + CYCLES] = initialGrid[i][j]

# printGrid(metagrid)
for i in range(CYCLES):
    metagrid = runCycle(metagrid)
    print(f'Cycle: {i + 1}')
    # printGrid(metagrid)

total = 0
for metalevel in range(len(metagrid)):
    for level in range(len(metagrid[metalevel])):
        for row in range(len(metagrid[metalevel][level])):
            for col in range(len(metagrid[metalevel][level][row])):
                if metagrid[metalevel][level][row][col] == '#':
                    total += 1

print(f'Total: {total}')
