# board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
board = {1: ' ', 2: ' ', 3: ' '}

tree = {}
scores = {}
player = 'O'
computer = 'X'


def printBoard(board):
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print('________')
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print('________')
    print(board[7] + ' |' + board[8] + ' |' + board[9])
    print("\n")


def part_finish(current_node):
    # Lignes
    if current_node[0] == current_node[1] and current_node[0] == current_node[2] and current_node[0] != 0:
        return current_node[0]
    elif current_node[3] == current_node[4] and current_node[3] == current_node[5] and current_node[3] != 0:
        return current_node[3]
    elif current_node[6] == current_node[7] and current_node[6] == current_node[8] and current_node[6] != 0:
        return current_node[6]
    # Colonnes
    elif current_node[0] == current_node[3] and current_node[0] == current_node[6] and current_node[0] != 0:
        return current_node[0]
    elif current_node[1] == current_node[4] and current_node[1] == current_node[7] and current_node[1] != 0:
        return current_node[1]
    elif current_node[2] == current_node[5] and current_node[2] == current_node[8] and current_node[2] != 0:
        return current_node[2]
    # Diagonales
    elif current_node[0] == current_node[4] and current_node[0] == current_node[8] and current_node[0] != 0:
        return current_node[0]
    elif current_node[6] == current_node[4] and current_node[6] == current_node[2] and current_node[6] != 0:
        return current_node[6]
    else:
        return 0


def full_board(current_node):
    for mark in current_node:
        if mark == 0:
            return False
    return True


def get_children(node):
    children = []

    mark = 1
    if not sum(node) == 0:
        mark = -1

    for pos in range(9):

        if node[pos] == 0:
            new_current_node = list(node)
            new_current_node[pos] = mark
            new_current_node = tuple(new_current_node)

            children.append(new_current_node)

    return children


def create_tree(tree, current_node):
    if part_finish(current_node) != 0:
        scores[current_node] = part_finish(current_node)
        tree[current_node] = part_finish(current_node)
        return

    if full_board(current_node):
        scores[current_node] = 0
        tree[current_node] = 0
        return

    mark = 1
    if not sum(current_node) == 0:
        mark = -1
    score = - mark

    if current_node not in tree:
        tree[current_node] = get_children(current_node)

    for child in tree[current_node]:
        create_tree(tree, child)
        if mark == 1:
            score = max(score, scores[child])
        else:
            score = min(score, scores[child])

    scores[current_node] = score


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

        if full_board():
            exit()
        if part_finish():
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



create_tree(tree, (0, 0, 0, 0, 0, 0, 0, 0, 0))

print(len(tree))
print(scores)

"""
while not partFinish():
    playerPlays()
    computerPlays()
"""
