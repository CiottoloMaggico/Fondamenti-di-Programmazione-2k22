# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Scrivere una funzione che data una matrice di interi, restituisce la matrice trasposta
# Ad esempio:
# 5 2 9    ->  5 3
# 3 1 0        2 1
#              9 0
def transpose(m : List[List[int]]) -> List[List[int]]:
    return [[m[row][column] for row in range(len(m))] for column in range(len(m[0]))]

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente alla somma fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       2 2 2
#     2 1 1   +    2 3 1   =   4 4 2
#     0 1 1        4 2 2       4 3 3
#     1 1 2        1 2 3       2 3 5
# Restituire None se le due matrici non possono essere sommate.
def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None

    return [[A[row][column] + B[row][column] for column in range(len(A[0]))] for row in range(len(A))]

# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente al prodotto fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       5  4 3
#     2 1 1   x    2 3 1   =   8  9 5
#     0 1 1        4 2 2       6  5 3
#     1 1 2                    11 9 6
# Restituire None se le due matrici non possono essere moltiplicate.
def matrix_matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0]) != len(B):
        return None

    return [[sum([A[row][column] * B[column][row_b] for column in range(len(B))]) for row_b in range(len(B[0]))] for row in range(len(A))]


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_rotate_right_and_flip_v(img_in: str, img_out : str):
    im = images.load(img_in)
    im_out = transpose(im)
    images.save(im_out, img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_invert_channels(img_in: str, img_out : str):
    img = images.load(img_in)
    return images.save([[img[row][pixel][::-1] for pixel in range(len(img[row]))] for row in range(len(img))], img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):
    img = images.load(img_in)
    return images.save([[list(map(lambda x: x//2, img[row][pixel])) for pixel in range(len(img[row]))] for row in range(len(img))], img_out)

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui la metà destra dell'immagine è scambiata con la metà sinistra.
# (Cioè, le colonne nel range [0, N/2] diventano le colonne [N/2, N] nella nuova immagine,
# e le colonne [N, N/2] nella vecchia immagine diventano le colonne [0, N/2] nella nuova immagine).
# Si può assumere che l'immagine abbia un numero di colonne divisibile per 2.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
# 1, 2, 3, 4 | 5, 6, 7, 8
def img_invert_half(img_in: str, img_out : str):
    img = images.load(img_in)
    range_split = len(img[0])//2

    for row in range(len(img)):
        for pixel in range(range_split):
            img[row][pixel], img[row][pixel+range_split] = img[row][pixel+range_split], img[row][pixel]

    return images.save(img, img_out)

def unicroma_screensaver(img_out: str, height: int, width: int, color: tuple[int]):
    return images.save([[color for _pixel in range(width)] for _row in range(height)], img_out)

def draw_line(img,  color: tuple[int], xstrt: int, ystrt: int, xend: int, yend: int):
    for row in range(ystrt, yend+1):
        for pixel in range(xstrt, xend+1):
            img[row][pixel] = color

    return img

def draw_cube(img_in: str, img_out: str, xstrt: int, ystrt: int, l: int, border: int, color: tuple[int]):
    img = images.load(img_in)
    img = draw_line(img, color, xstrt, ystrt, xstrt+l, ystrt+border)
    img = draw_line(img, color, xstrt, ystrt+l, xstrt+l, ystrt+l+border)
    img = draw_line(img, color, xstrt+l, ystrt, xstrt+l+border, ystrt+l+border)
    img = draw_line(img, color, xstrt, ystrt, xstrt+border, ystrt+l)

    return images.save(img, img_out)

def draw_pixel(img: list[list[tuple]], x: int, y: int, color: tuple[int]):
    img[y][x] = color
    return img

def draw_slope(img_in: str, img_out: str, xstrt: int, ystrt: int, xend: int, yend: int, color: tuple[int]):
    img = images.load(img_in)
    if xstrt > xend:
        xstrt, ystrt, xend, yend = xend, yend, xstrt, ystrt
    m = (yend - ystrt)/(xend-xstrt)
    q = ((xend*ystrt)-(xstrt*yend))/(xend-xstrt)
    cx, cy = xstrt, ystrt
    while (cx, cy) != (xend, yend):
        img = draw_pixel(img, cx, int(cy), color)
        cx += 1
        cy = m*cx+q

    return images.save(img, img_out)

def draw_circle(img_in: str, img_out: str, xcenter: int, ycenter: int, radius: int, color: tuple[int]):
    img = images.load(img_in)
    E, X, Y = -radius, radius, 0
    e, x, y = -radius, 0, radius

    while Y <= X:
        draw_pixel(img, xcenter+X, ycenter+Y, color)
        draw_pixel(img, xcenter-X, ycenter-Y, color)
        draw_pixel(img, xcenter+X, ycenter-Y, color)
        draw_pixel(img, xcenter-X, ycenter+Y, color)
        draw_pixel(img, xcenter+x, ycenter+y, color)
        draw_pixel(img, xcenter-x, ycenter-y, color)
        draw_pixel(img, xcenter+x, ycenter-y, color)
        draw_pixel(img, xcenter-x, ycenter+y, color)
        E += 2*Y+1
        Y += 1
        e += 2*x+1
        x += 1
        if E >= 0:
            E -= 2*X-1
            X -= 1
        if e >= 0:
            e -= 2*y-1
            y -= 1


    return images.save(img, img_out)



# unicroma_screensaver("unicroma.png", 1000, 1000, (255,255,255))
# draw_line("unicroma.png", "img_white_line.png", (0,0,0), 700, 300, 750, 600)
# draw_cube("unicroma.png", "cube.png", 400, 400, 100, 30, (0,0,0))
# draw_pixel("unicroma.png", 500, 500, (255, 0, 0))
# draw_slope("unicroma.png", "slope.png", 700, 600, 800, 100, (0,0,0))
draw_circle("unicroma.png", "circle.png", 500, 500, 50, (0,0,0))
# Test funzioni
# check_test(transpose, [[5, 3], [2, 1]], [[5, 2], [3, 1]])
# check_test(transpose, [[5, 3], [2, 1], [9, 0]], [[5, 2, 9], [3, 1, 0]])
# check_test(transpose, [[5, 3]], [[5], [3]])
# check_test(transpose, [[5], [3]], [[5, 3]])
# check_test(matrix_matrix_sum, [[2, 2, 2], [4, 4, 2], [4, 3, 3], [2, 3, 5]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2], [1, 2, 3]])
# check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2], [2, 3], [4, 2], [1, 2]])
# check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
# check_test(matrix_matrix_mul, [[5, 4, 3], [8, 9, 5], [6, 5, 3], [11, 9, 6]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
# check_test(matrix_matrix_mul, [[5], [8], [6], [11]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1], [2], [4]])
# check_test(matrix_matrix_mul, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1]])
# img_rotate_right_and_flip_v("img1.png", "img1_rotate_flip.png")
# img_invert_channels("img1_invert_channels.png", "img1_invert_channels.png")
# img_quantize("img1_quantized.png", "img1_quantized.png")
# img_invert_half("img1.png", "img1_inverted_half.png")