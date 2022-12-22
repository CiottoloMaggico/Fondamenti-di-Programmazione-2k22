# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images
import math


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


# Definire una funzione che crea un'immagine di dimensione 600x600 (pixels), 
# interamente bianca.
# La funzione prende i seguenti parametri:
#  - points: una lista di coppie, che rappresentano dei punti
#            all'interno dell'immagine. I punti sono rappresentati con coordinate 
#            (x, y), dove (0, 0) è l'angolo in basso a sinistra dell'immagine
#  - d: la dimensione dei punti. Ad esempio, se d=5, i punti sono dei quadrati 5x5.
#       Si può assumere che d sia sempre dispari
#  - c: una tupla rappresentante un colore
#  - outfile: il nome del file su cui scrivere l'immagine
#
# La funzione deve disegnare i punti, e le linee che connettono due punti consecutivi 
# (l'ultimo punto della lista verrà connesso col primo).
# Ad esempio, se:
#  - points = [(10, 30), (14, 99), (0, 2)]
#  - d = 5
#  - c = (0, 0, 0)
#
# La funzione disegnare un punto in ognuna delle coordinate specificate in points. Il 
# punto sarà un quadrato di lato 5x5 (pixels), centrato nel punto specificato nelle coordinate
# e con colore c. Dopodichè, la funzione disegnerà una linea 
# che connette il punto (10, 30) al punto (14, 99), e una linea che connette il punto
# (14, 99) al punto (0, 2). Il colore delle linee è lo stesso dei punti.
#
# Per disegnare una linea fra un generico punto (x1, y1) e un punto (x2, y2), bisogna colorare tutti i punti 
# (x, y), tali che la distanza fra (x1, y1) e (x, y), sommata alla distanza fra (x, y) e (x2, y2), è uguale
# alla distanza fra (x1, y1) e (x2, y2). Per calcolare la distanza, usare la formula 
# distanza = sqrt((x1-x2)**2 + (y1-y2)**2). Fare attenzione alla conversione da float a interi e viceversa.
# (L'eguaglianza dotrebbe essere non un "uguale" ma un "quasi uguale")
#
# Vedere l'esempio test_1.png.
#
# Provare a sviluppare una soluzione ottimizzata in cui si evita di scandire tutti i pixel dell'immagine
# per disegnare le linee.
def vertical(img_in, x, y1, y2):
    y1, y2 = max([y1, y2]), min([y1, y2])
    for line in range(abs(y1-y2)):
        img_in[y2+line][x] = (0,0,0)
    return img_in

def orizzontal(img_in, y, x1, x2):
    x1, x2 = max([x1, x2]), min([x1, x2])
    for x in range(abs(x1-x2)):
        img_in[y][x2+x] = (0,0,0)
    return img_in

def image_creator(width, height, color):
    new_image = [[color for x_ in range(width)] for y_ in range(height)]
    return new_image

def square_from_point(in_img, x, y, d, c):
    x, y = x-d//2, y+d//2
    for line in range(1,d):
        for pixel in range(0,d-1):
            in_img[y-line][x+pixel] = c
    return in_img

def slope_line(in_img, x1, y1, x2, y2, c):
    xdist, ydist = abs(x1-x2), abs(y1-y2)
    directionx, directiony = -1 if x2 < x1 else 1, -1 if y2 < y1 else 1
    absolute_distance = math.sqrt(xdist**2+ydist**2)

    for y in range(ydist):
        y = directiony*y+y1
        for x in range(xdist):
            x = directionx*x+x1
            distance = math.sqrt((x1-x)**2+(y1-y)**2)+math.sqrt((x-x2)**2+(y-y2)**2)
            if absolute_distance-0.01 <= distance <= absolute_distance+0.01:
                in_img[y][x] = c

    return in_img


def img_draw(points: List[Tuple[int]], d: int, c: Tuple[int], outfile: str):
    background = image_creator(600, 600, (255,255,255))
    points = list(map(lambda x: (x[0], abs(600-x[1])), points))
    for x,y in points:
        background = square_from_point(background, x, y, d, c)

    point_next, point_curr = points[1], points[0]
    background = slope_line(background, points[-1][0], points[-1][1], points[0][0], points[0][1], c)
    for i in range(1, len(points)):
        if point_curr[0] == point_next[0]:
            background = vertical(background, point_curr[0], point_curr[1], point_next[1])
        elif point_curr[1] == point_next[1]:
            background = orizzontal(background, point_curr[1], point_curr[0], point_next[0])
        background = slope_line(background, point_curr[0], point_curr[1], point_next[0], point_next[1], c)
        point_curr = point_next
        if i < len(points)-1:
            point_next = points[i+1]


    images.save(background, outfile)


# Implementare una funzione che, sfruttando la funzione sviluppata precedentemente, disegni un quadrato
# da salvare sul file outfile.
def square(outfile: str):
    img = images.load("test_1.png")
    img = square_from_point(img, 300, 300, 20, (0,0,0))
    images.save(img, outfile)

# Implementare una funzione che, sfruttando la funzione sviluppata precedentemente, disegni una stella a 5 punte,
# da salvare sul file outfile.
def five_point_star(outfile: str):
    points = [[300, 100], [300+25, 50], [300-25, 80], [300+25, 80], [300-25, 50]]
    return img_draw(points, 5, (0,0,0), outfile)

print(img_draw([(100, 320), (141, 99), (50, 50)], 15, (0, 0, 0), "test_1.png"))
img_draw([(0, 320), (141, 99), (500, 50), (14, 26), (500, 12), (300, 152)], 15, (0, 255, 0), "test_2.png")
square("square.png")
five_point_star("fpstar.png")

