# board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
board = {1: ' ', 2: ' ', 3: ' '}

tree = {}
player = 'O'
computer = 'X'


def printBoard(board):
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print('________')
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print('________')
    print(board[7] + ' |' + board[8] + ' |' + board[9])
    print("\n")


def partFinish(current_node):
    # Lignes
    if (current_node[0] == current_node[1] and current_node[0] == current_node[2] and current_node[0] != 0):
        return True
    elif (current_node[3] == current_node[4] and current_node[3] == current_node[5] and current_node[3] != 0):
        return True
    elif (current_node[6] == current_node[7] and current_node[6] == current_node[8] and current_node[6] != 0):
        return True
    # Colonnes
    elif (current_node[0] == current_node[3] and current_node[0] == current_node[6] and current_node[0] != 0):
        return True
    elif (current_node[1] == current_node[4] and current_node[1] == current_node[7] and current_node[1] != 0):
        return True
    elif (current_node[2] == current_node[5] and current_node[2] == current_node[8] and current_node[2] != 0):
        return True
    # Diagonales
    elif (current_node[0] == current_node[4] and current_node[0] == current_node[8] and current_node[0] != 0):
        return True
    elif (current_node[6] == current_node[4] and current_node[6] == current_node[2] and current_node[6] != 0):
        return True
    else:
        return False


def fullBoard(current_node):
    for mark in current_node:
        if mark == 0:
            return False
    return True


def createTree(tree, current_node):

    if partFinish(current_node) or fullBoard(current_node):
        tree[current_node] = []
        return

    mark = 1
    if not sum(current_node) == 0:
        mark = -1

    for pos in range(len(current_node)):

        if current_node[pos] == 0:

            new_current_node = list(current_node)
            new_current_node[pos] = mark
            new_current_node = tuple(new_current_node)

            if current_node not in tree.keys():
                tree[current_node] = [new_current_node]
            else:
                tree[current_node].append(new_current_node)
            createTree(tree, new_current_node)


def computerPlays():
    print("COMPUTER PLAYS :")


def freePosition(position):
    if board[position] == ' ':
        return True
    else:
        return False


def savePosition(letter, position):
    if freePosition(position):
        board[position] = letter
        printBoard(board)

        if fullBoard():
            exit()
        if partFinish():
            if letter == 'X':
                print("Computer wins")
                exit()
            else:
                print("Player wins")
                exit()

    else:
        print("Position already filled. Try again !")
        position = int(input("Please enter new position:  "))
        savePosition(letter, position)


def playerPlays():
    print("PLAYER PLAYS :")
    position = int(input("Enter the position:  "))
    savePosition(player, position)


createTree(tree, (0, 0, 0, 0, 0, 0, 0, 0, 0))

print(len(tree))

"""
while not partFinish():
    playerPlays()
    computerPlays()
"""
