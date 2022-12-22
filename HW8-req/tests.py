
with open("boards/01.txt", "r") as file:
    board = [tuple(line.split()) for line in file.readlines()]
    print(board)
    print("".join(["".join(_) for _ in board]))