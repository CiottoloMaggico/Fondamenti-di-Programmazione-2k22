#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra
funzione usata per la soluzione deve essere ricorsiva.

'''

def open_board(path: str):
    with open(path, "r", encoding="utf8") as board:
        return [tuple(line.split()) for line in board.readlines()]

def check_winner(board, state):
    black, white = 0, 0
    for line in board:
        black += line.count("B")
        white += line.count("W")

    if black > white:
        state = [state[0]+1, state[1], state[2]]
    elif white > black:
        state = [state[0], state[1]+1, state[2]]
    elif white == black:
        state = [state[0], state[1], state[2]+1]
    return state

def valid_position(x, y, player, opponent, table):
    board = [list(line) for line in table]
    valid = False
    flips = [
            (0, -1), # N
            (-1, -1), # NW
            (-1, 0), # W
            (-1, 1), # SW
            (0, 1), #S
            (1, 1), #SE
            (1, 0), #E
            (+1, -1)# NE
    ]
    if board[y][x] != ".":
        return False

    for coords in flips:
        temp_x, temp_y = coords
        if ((y+temp_y >= 0 and y+temp_y < len(board)) and (x+temp_x >= 0 and x+temp_x < len(board[0]))) and board[y+temp_y][x+temp_x] == opponent:
            board[y+temp_y][x+temp_x] = player
            valid = True

    if valid:
        board[y][x] = player
        return board
    return False

def tree_builder(table, player, opponent, state= (0, 0, 0)):
        empty = [(x, y) for x in range(len(table[0])) for y in range(len(table)) if table[y][x] == "."]
        all_invalid = True
        if len(empty) == 0:
            return check_winner(table, state)

        player, opponent = opponent, player

        for position in empty:
            x, y = position
            is_valid = valid_position(x, y, player, opponent, table)
            if type(is_valid) == list:
                all_invalid = False
                state = tree_builder([tuple(line) for line in is_valid], player, opponent, state)

        if all_invalid:
            return check_winner(table, state)
        return state

def dumbothello(filename : str) -> tuple[int,int,int] :
    board = open_board(filename)
    return tuple(tree_builder(board, "W", "B"))

if __name__ == "__main__":
    R = dumbothello("boards/03.txt")
    print(R)








