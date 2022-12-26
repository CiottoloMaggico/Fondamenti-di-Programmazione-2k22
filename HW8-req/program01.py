def valid_position(index, player, opponent, board, params):
    offsets, board = [-params[0], +params[0], +1, -1, -params[0]+1, -
                      params[0]-1, +params[0]+1, +params[0]-1], board.copy()

    for offset in offsets:
        temp_index = index + offset
        print(temp_index)
        if 0 <= temp_index < params[1] and board[temp_index] == opponent:
            board[temp_index] = player
            board[index] = player

    if board[index] != ".":
        return board
    return False


def tree_builder(table, player, opponent, params, empties, score, cache={}, masterkey="", a=0, b=0, c=0):
    if not empties:
        disks = {"B": masterkey.count("B"), "W": masterkey.count("W")}
        return score[max(disks, key=disks.get) if not disks["B"] == disks["W"] else "ODD"], cache

    for x, y in empties.copy():
        board = valid_position(x, y, opponent, player, table, params)
        if board is not False:
            key = "".join(["".join(line) for line in board])
            if key in cache:
                points = cache[key]
            else:
                empties.remove((x, y))
                points, cache = tree_builder(
                    board, opponent, player, params, empties, score, cache, key)
                cache[key] = points
                empties += (x, y),

            a, b, c = a+points[0], b+points[1], c+points[2]

    if not (a+b+c):
        disks = {"B": masterkey.count("B"), "W": masterkey.count("W")}
        return score[max(disks, key=disks.get) if not disks["B"] == disks["W"] else "ODD"], cache

    return (a, b, c), cache


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename, "r") as board:
        board = [line.split() for line in board.readlines()]
    params = len(board[0])+1
    board = list(
        map(str, "".join(["".join(line)+" " for line in board])))

    params = (params, len(board))
    empties = [index for index in range(len(board)) if board[index] == "."]
    print(board)
    is_valid = valid_position(6, "B", "W", board, params)
    # final, cache = tree_builder(board, "W", "B", params, empties, {
    #                             "B": (1, 0, 0), "W": (0, 1, 0), "ODD": (0, 0, 1)})
    return is_valid, board


print(dumbothello("boards/01.txt"))