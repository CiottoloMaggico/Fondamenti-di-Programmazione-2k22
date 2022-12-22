import turtle
from random import randint
from time import sleep


def susi_one(n):
    result = 0
    current = 0
    target = n
    
    while target > 0:
        if target < len(str(current))-1:
            print(str(current), target)
            result = str(current)[target]
        
        target -= len(str(current))
        current += 1
    
    return result

# print(susi_one(200))

def susi_two(n):
    result = 0
    
    for i in range(1, n+1):
        corretta = bool(i % 3 == 0)
        data = bool(i % 4 != 0)
        
        if corretta == data:
            result += 1
        
        
    return result

# print(susi_two(100))


def draw_trunk(t, lunghezza):
    'Disegno un tratto di colore casuale'
    # TODO
    # cambio colore a caso
    R = 123
    G = 123
    B = 123
    t.color((0.5,1,0.2))
    # abbasso la penna
    t.pendown()
    # mi muovo in avanti di lunghezza pixel
    t.forward(lunghezza)
    # alzo la penna
    t.penup()
    # NOTA: ora sono all'estremo opposto del tronco
    
def draw_leaf(t):
    'disegno una foglia col colore corrente'
    # TODO
    # abbasso la penna
    t.pendown()
    # disegno un pallino
    t.dot()
    # alzo la penna
    t.penup()

def albero(t, tronco, angolo, livelli):
    'disegno un albero con un certo tronco iniziale e # di livelli'
    # TODO
    if livelli == 0:
        draw_leaf(t)
    else:
        # disegno il tronco (e mi sposto alla fine)
        draw_trunk(t, tronco)
        # mi giro a sinistra
        t.left(angolo)
        # disegno il ramo sinistro, più piccolo 80%
        albero(t, tronco * 0.8, angolo, livelli-1)
        # mi giro a destra
        t.right(angolo*2)
        # disegno il ramo destro, più piccolo 70%
        albero(t, tronco * 0.7, angolo, livelli-1)
        # torno nella direzione iniziale
        t.left(angolo)
        # torno alla base del tronco
        t.back(tronco)
        
t = turtle.Turtle()   
t.speed(0)     
        
albero(t,100,30,10)