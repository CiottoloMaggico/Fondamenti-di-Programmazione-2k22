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


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine corrispondente in scala di grigi.
# Per fare ciò, se R è il canale del rosso, G del verde, e B del blu, rimpiazzare ogni canale
# con il valore 0.2126*R + 0.7152*G + 0.0722*B.
# Attenzione: Il valore di ciascun canale deve essere un intero.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_grayscale(img_in: str, img_out: str):
    img = images.load(img_in)
    new_img = [list(map(lambda x: (int(x[0]*0.2989)+int(x[1]*0.5870)+int(x[2]*0.114), int(x[0]*0.2989)+int(x[1]*0.5870)+int(x[2]*0.114), int(x[0]*0.2989)+int(x[1]*0.5870)+int(x[2]*0.114)), img[row])) for row in range(len(img))]
    return images.save(new_img, img_out)


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# ruota l'immagine (tenendo fisso il centro) di un certo numero di gradi centigradi
# specificato come parametro (theta).
# Per fare ciò, utilizzare la seguente formula:
#   - Se ruotiamo l'immagine di un angolo theta, il pixel che si trova alle coordinate (x, y),
#     nell'immagine ruotata si troverà alle coordinate (x*cos(theta) + y*sin(theta), -x*sin(theta) + y*cos(theta))
# Attenzione: controllare la documentazione per vedere cosa richiedono in input le funzioni
# math.sin e math.cos
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_rotate(img_in: str, theta: float, img_out: str):
    pass

# Definire una funzione che disegna un cerchio centrato in (x,y) e di raggio r,
# su una immagine presa in input e la ri-scrive in output.
# Per disegnare il cerchio, testiamo se un punto è all'interno del cerchio o no,
# guardando se la distanza dal center è <= raggio. Nel caso settiamo il colore c.
# Il centro di ogni pixel è translato di 0.5 rispetto agli indici dei pixels.
def img_circle(img_in: str, x: float, y: float, r: float, c: Tuple, img_out: str):
    img = images.load(img_in)

    # for row in range(len(img)):
    #     for pixel in range(len(img[0])):
    #         if math.sqrt((pixel-x)**2+(row-y)**2) <= r:
    #             img[row][pixel] = c

    return images.save([[c if math.sqrt((pixel-x)**2+(row-y)**2) <= r else img[row][pixel] for pixel in range(len(img[0]))] for row in range(len(img))], img_out)


# Definire una funzione che applica aggiunstamenti di colore ad una immagine.
# In particolare, applichiamo nel'ordine: (a) tinta, (b) contrasto, (c) saturazione.
# Per farlo, priam riportiamo i colori in [0,1] float, poi applichiamo gli updates,
# e poi torniamo in [0,255] intero.
# (a) tinta: pixel *= t
# (b) contrasto: pixel = (pixel - 0.5) * c + 0.5
# (c) saturazione: pixel = (pixel - gray(pixel)) * s + gray(pixel)
def truncate(color: int):
    if color > 255:
        return 255
    if color < 0:
        return 0
    return int(color)

def apply_gray(x: tuple[int]):
    # 0.2126*R + 0.7152*G + 0.0722*B.
    return x[0]*0.2126 + x[1]*0.7152 + x[2]*0.0722

def img_colorgrade(img_in: str, t: tuple, c: float, s: float, img_out: str):
    img = images.load(img_in)

    # Tinta
    img = [list(map(lambda x: ((x[0]/255)*t[0], (x[1]/255)*t[1], (x[2]/255)*t[2]), img[row])) for row in range(len(img))]
    # Contrasto
    img = [list(map(lambda x: ((x[0] - 0.5) * c + 0.5, (x[1] - 0.5) * c + 0.5, (x[2] - 0.5) * c + 0.5), img[row])) for row in range(len(img))]
    # Saturazione
    img = [list(map(lambda x: ((x[0] - apply_gray(x)) * s + apply_gray(x), (x[1] - apply_gray(x)) * s + apply_gray(x), (x[2] - apply_gray(x)) * s + apply_gray(x)), img[row])) for row in range(len(img))]

    img = [list(map(lambda x: (truncate(x[0]*255), truncate(x[1]*255), truncate(x[2]*255)), img[row])) for row in range(len(img))]

    return images.save(img, img_out)


# Definire una funzione che crea un mosaico sui pixel di una immagine. Il mosaico
# ha celle di larghezza n. Per questo esercizio usiamo un colore del quadratino e
# non ci preoccupiamo di fare la media. Inoltre disegniamo anche delle linee nere
# intorno a ogni cella del mosaico.
def oriz_line(img: tuple[int], y: int):
    img[y] = list(map(lambda x: (0,0,0), img[y]))
    return img

def vert_line(img: tuple[int], x:int):
    for row in range(len(img)):
        img[row][x] = (0,0,0)
    return img

def mosaicaze(img: tuple[int], row: int, pixel: int, n: int):
    center = n//2
    for y in range(row, row+n):
        for x in range(pixel, pixel+n):
            img[y][x] = img[row][pixel+center]

    return img


def img_mosaic(img_in: str, n: int, img_out: str):
    img = images.load(img_in)
    x_fixed = (len(img[0]) % n)//2 + (len(img[0]) % n) % 2
    y_fixed = (len(img) % n)//2 + (len(img) % n) % 2

    for row in range(y_fixed, len(img)-y_fixed, n):
        for pixel in range(x_fixed, len(img[0])-x_fixed, n):
            img = mosaicaze(img, row, pixel, n)

            img = vert_line(img, pixel)
        img = oriz_line(img, row)

    return images.save(img, img_out)


# Test funzioni
# img_grayscale("img1.png", "img1_grayscale.png")
# for angle in [-30, 15, 30, 45, 480, -500]:
#     img_rotate("img1.png", angle, "img1_rotated_" + str(angle) + ".png")
# img_circle("img1.png", 100, 100, 25, (255, 255, 0), "img1_circle.png")
# img_colorgrade("img1.png", (0.1, 1.0, 0.9), 2, 1, "img_colorgrade1.png")
# img_colorgrade("img1.png", (1.0, 1.0, 1.0), 2, 1, "img_colorgrade2.png")
# img_colorgrade("img1.png", (1.0, 1.0, 1.0), 1, 2, "img_colorgrade3.png")
# img_colorgrade("img1.png", (0.8, 1.0, 0.8), 2, 0.7, "img_colorgrade4.png")
# img_colorgrade("img1.png", (1.0, 1.0, 1.0), 1, 100, "img_colorgrade5.png")
# img_mosaic("img1.png", 8, "img_mosaic.png")
