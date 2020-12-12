seats = [list(line.rstrip('\n')) for line in open('data/data.txt')]

for i in range(len(seats)):
    seats[i].insert(0, '.')
    seats[i].append('.')

floorRow = ['.'] * len(seats[0])
seats.insert(0, floorRow)
seats.append(floorRow)


def copyBoard(board):
    newBoard = []
    for row in board:
        newRow = []
        for seat in row:
            newRow.append(seat)
        newBoard.append(newRow)
    return newBoard


def boardsAreEqual(oldBoard, newBoard):
    for row in range(len(oldBoard)):
        for col in range(len(oldBoard[row])):
            if oldBoard[row][col] != newBoard[row][col]:
                return False
    return True


def countViewline(row, col, board):
    freeCount = 0
    occupiedCount = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            seat = board[row + i][col + j]
            multiplier = 1
            while seat == '.' \
                    and 0 < (row + i * multiplier) < (len(board)) \
                    and 0 < (col + j * multiplier) < (len(board[row + i * multiplier])):
                seat = board[row + i * multiplier][col + j * multiplier]
                multiplier += 1

            if seat == 'L':
                freeCount += 1
            elif seat == '#':
                occupiedCount += 1
    return freeCount, occupiedCount


def nextTurn(board):
    newBoard = copyBoard(board)
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[row]) - 1):
            position = board[row][col]
            if position == '.':
                continue

            freeCount, occupiedCount = countViewline(row, col, board)
            if position == 'L' and occupiedCount == 0:
                # print(f'Changing row {row} col {col} to #')
                newBoard[row][col] = '#'
            elif position == '#' and occupiedCount >= 5:
                # print(f'Changing row {row} col {col} to L')
                newBoard[row][col] = 'L'
    return newBoard


def countOccupied(board):
    count = 0
    for row in board:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def printBoard(board):
    for row in board:
        print(''.join(row))
    print()

nextTurnBoard = nextTurn(seats)
while not boardsAreEqual(seats, nextTurnBoard):
    seats = nextTurnBoard
    nextTurnBoard = nextTurn(seats)

print(countOccupied(seats))