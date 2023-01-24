def valid_position(x, y, player, opponent, board, params):
    flips, board = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1),
                    (1, 1), (1, 0), (+1, -1)], list(map(list.copy, board))

    for temp_x, temp_y in flips:
        x_, y_ = x+temp_x, y+temp_y
        if ((0 <= x_ < params[0]) and (0 <= y_ < params[1])) and board[y_][x_] == opponent:
            board[y_][x_] = player
            board[y][x] = player

    if board[y][x] != ".":
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
    params = (len(board[0]), len(board))
    empties = [(x, y) for x in range(params[0])
               for y in range(params[1]) if board[y][x] == "."]
    final, cache = tree_builder(board, "W", "B", params, empties, {
                                "B": (1, 0, 0), "W": (0, 1, 0), "ODD": (0, 0, 1)})
    return final
