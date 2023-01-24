def valid_position(index, player, opponent, board, params):
    offsets = [-params[0], +params[0], +1, -1, -params[0]+1, -
               params[0]-1, +params[0]+1, +params[0]-1]

    for offset in offsets:
        temp_index = index + offset
        if 0 <= temp_index < params[1] and board[temp_index] == opponent:
            board[temp_index] = player
            board[index] = player

    if board[index] != ".":
        return board
    return False


def tree_builder(table, player, opponent, params, empties, score, cache={}):
    a, b, c = 0, 0, 0
    if not empties:
        disks = {"B": table.count("B"), "W": table.count("W")}
        return score[max(disks, key=disks.get) if not disks["B"] == disks["W"] else "ODD"], cache

    for index in empties.copy():
        board = valid_position(index, opponent, player, table.copy(), params)
        if board is not False:
            key = "".join(board)
            if key not in cache:
                empties.remove(index)
                points, cache = tree_builder(
                    board, opponent, player, params, empties, score, cache)
                cache[key] = points
                empties += index,
            else:
                points = cache[key]

            a, b, c = a+points[0], b+points[1], c+points[2]

    if not (a+b+c):
        disks = {"B": table.count("B"), "W": table.count("W")}
        return score[max(disks, key=disks.get) if not disks["B"] == disks["W"] else "ODD"], cache

    return (a, b, c), cache


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename, "r") as board:
        board = list(map(str, "".join(
            ["".join(line.split())+" " for line in board.readlines()])))

    params = (board.index(" ")+1, len(board))
    empties = [index for index in range(params[1]) if board[index] == "."]
    final = tree_builder(board, "W", "B", params, empties, {
                                "B": (1, 0, 0), "W": (0, 1, 0), "ODD": (0, 0, 1)})
    return final[0]