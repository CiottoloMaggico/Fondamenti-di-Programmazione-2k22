# Ignorare le righe fino alla 31
from dataclasses import is_dataclass
from re import I
from typing import Any, Callable, List
import sys

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
        test_outcome = "succeeded" if (result==expected) else "failed"
        color = bcolors.OKGREEN if (result==expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.
def check_pwd(pwd: str) -> bool:
    check_letters, check_number, check_spchar, check_lenght, unknown = [False, False], False, False, False, False
    
    if not 6 <= len(pwd) <= 16 or pwd.isdigit() or pwd.isalpha():
        return False
    
    check_lenght = True
    
    for i in pwd:
        if i.isupper():
            check_letters[0] = True
            continue
        elif i.islower():
            check_letters[1] = True
            continue
        elif i.isdigit():
            check_number = True
            continue
        elif i in ["$", "#", "@"]:
            check_spchar = True
            continue
        unknown = True
        break
    
    if all([all(check_letters), check_number, check_spchar, check_lenght]) and not unknown:
        return True
    return False        
    

# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
def tuple_ex(t: tuple) -> tuple:
    return tuple(list([t[2]+1, t[0]-1, t[1]+2]))

# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    return list(set(a) & set(b))

# Scrivere una funzione che data una lista contenente valori >= 0, 
# crei una nuova lista contentente soltanto gli elementi della lista 
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# (Il primo elemento non viene quindi mai inserito)
# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito
#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5. Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista
#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista
#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6. Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
def remove_avg(a: list) -> list:
    def average(list_to_average):
        print(list_to_average)
        return sum(list_to_average) / len(list_to_average)
    
    result = []
    
    for i in range(len(a)):
        if i != 0:
            if a[i] > 2*average(a[:i]):
                result.append(a[i])
        
    return result

# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
    # 1, 1, 1, 3
    # 0, 1, 2, 3
    a.sort()
    res = []
    i = 0
    
    while i != len(a):
        num_of_num = a.count(a[i])
        res.append((a[i], num_of_num))
        i += num_of_num
        
    return res

# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:
    if not len(a):
        return True
    
    for i in range(len(a)//2+1):
        if a[i] != a[-(i+1)]:
            return False
    return True
    
        

# Scrivere una funzione che prende in input una lista, e 
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
def is_sorted(a: list) -> bool:
    increasing, decreasing = True, True

    for index in range(len(a)-1):
        if a[index] > min(a[index+1:]):
            increasing = False
        elif a[index] < max(a[index+1:]):
            decreasing = False
            
    if increasing is False and decreasing is False:
        return False
    return True


# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    peak = 0
    # 1 2 3 4 5 4 3 2
    # 5 4 3 2 1 2 3 4
    
    for index in range(1, len(a)-1):
        if a[index-1] < a[index] and a[index] > a[index+1]:
            peak += 1
        elif a[index-1] > a[index] and a[index] < a[index+1]:
            peak += 1

    if peak == 1:
        return True
    return False
        

# Test funzioni
# check_test(check_pwd, False, "a")
# check_test(check_pwd, False, "000000000000000000")
# check_test(check_pwd, False, "almeno6")
# check_test(check_pwd, False, "Aa@09asng2/")
# check_test(check_pwd, True, "Aa@09asng2")
# check_test(tuple_ex, (3, -2, 1), (-1, -1, 2))
# check_test(intersect, [2, 3], [1, 2, 3], [2, 3, 4])
# check_test(intersect, [], [1, 2, 3], [10, 11, 12])
# check_test(intersect, [], [1, 2, 3], [])
# check_test(intersect, [], [], [1, 2, 3])
# check_test(remove_avg, [10], [5, 3, 10, 0])
# check_test(remove_avg, [20, 1000], [5, 20, 10, 1000])
# check_test(remove_avg, [], [])
# check_test(frequency, [(1, 1), (4, 2), (5, 1)], [5, 4, 1, 4])
# check_test(frequency, [(0, 1), (23, 3), (99, 1)], [23, 99, 0, 23, 23])
# check_test(is_palindrome, True, [])
# check_test(is_palindrome, True, [1])
# check_test(is_palindrome, True, [1, 2, 8, 2, 1])
# check_test(is_palindrome, True, [1, 2, 8, 8, 2, 1])
# check_test(is_palindrome, False, [1, 3, 8, 8, 2, 1])
# check_test(is_sorted, True, [1])
# check_test(is_sorted, True, [1, 1, 1])
# check_test(is_sorted, True, [1, 2, 3, 4])
# check_test(is_sorted, True, [4, 3, 2, 1])
# check_test(is_sorted, True, [1, 1, 2, 3, 3, 4])
# check_test(is_sorted, True, [4, 4, 3, 2, 2, 1])
# check_test(is_sorted, False, [1, 1, 3, 3, 2])
# check_test(is_sorted, False, [4, 4, 3, 3, 5])
# check_test(is_sorted, False, [1, 1, 4, 4, 3, 3, 5])
# check_test(is_sorted_half, False, [1, 2, 3])
# check_test(is_sorted_half, False, [3, 2, 1])
# check_test(is_sorted_half, True, [1, 3, 2])
# check_test(is_sorted_half, True, [3, 1, 2])
# check_test(is_sorted_half, False, [1, 2, 5, 6, 8, 9, 1, 3, 2])
