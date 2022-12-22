import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:

    moves = {"N": (0, -1), "NW": (-1, -1), "W": (-1, 0), "SW": (-1, 1), "S": (0, 1), "SE": (1, 1), "E": (1, 0), "NE": (+1, -1)}
    snake, commands = [position], tuple(commands.split())
    x, y = position
    background = images.load(start_img)
    max_width, max_height = len(background[0]), len(background)
    x, y = position

    for command in commands:
        _x, _y = (x+moves[command][0]) % max_width, (y+moves[command][1]) % max_height
        if background[y][_x] == background[_y][x] == (0, 255, 0):
            break
        x, y = _x, _y

        snake += (x, y),

        if set((255, 0, 0)) == set(background[y][x]):
            snake.pop(0)
            break
        elif background[y][x] != (255, 128, 0):
            xg_, yg_ = snake.pop(0)
            background[yg_][xg_] = (128, 128, 128)

        background[y][x] = (0, 255, 0)

    images.save(background, out_img)
    return len(snake)
