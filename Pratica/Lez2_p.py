from dataclasses import replace
from os import remove
from string import whitespace
from typing import Any, Callable, List
import time

st = time.time()


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return f"Ciao {name}, Buona giornata!"


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    count = 0
    start, end = 0, 0
    is_strip_start, is_strip_end = False, False
      
    while True:
        if is_strip_start and is_strip_end:
            return string[start:end]
        elif count == len(string):
            return ""
        
        if string[count] != " " and not is_strip_start:
            is_strip_start = True
            start = count
        
        if string[-(count+1)] != " " and not is_strip_end:
            is_strip_end = True
            end = len(string)-count
        
        count += 1        
        

# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    splitted = []
    prev = 0
    curr = 0
    if not len(characters):
        return [strip_whitespace(string[prev:curr])]
    
    while True:
        if curr >= len(string):
            if string[prev:curr] != characters and len(strip_whitespace(string[prev:curr])):
                splitted.append(string[prev:curr])
                return splitted
            return splitted
        
        if string[curr:curr+len(characters)] == characters:
            if len(strip_whitespace(string[prev:curr])):
                splitted.append(string[prev:curr])
            curr, prev = curr+len(characters), curr+len(characters)
        else:
            curr += 1
            
# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    string_manipulated = split_string(string, find)
    prefix, suffix = "", ""

    if string[:len(find)] == find:
        prefix = replace
    if string[-(len(find)):] == find:
        suffix = replace
        
    return prefix + replace.join(string_manipulated) + suffix    


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.

def shifter(in_letter, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if in_letter == " ":
        return in_letter
    
    if alphabet.index(in_letter)+offset >= len(alphabet):
        rest = (alphabet.index(in_letter)+offset) % len(alphabet)
        return alphabet[rest]
    
    return alphabet[alphabet.index(in_letter)+offset]

def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    shifted = ""
    if decrypt:
        offset = -(offset)
        for letter in string:
            shifted += shifter(letter, offset)
        return shifted
    
    for letter in string:
        shifted += shifter(letter, offset)
    return shifted                    

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
    letter = {"Uppercase": 0, "Lowercase": 0}
    number, special = 0, 0
    
    if 6 <= len(pwd) <= 16:
        for i in pwd:
            if 65 <= ord(i) <= 90:
                letter["Uppercase"] += 1
            elif 97 <= ord(i) <= 123:
                letter["Lowercase"] += 1
            elif i.isdigit():
                number += 1
            elif i in ["$", "#", "@"]:
                special += 1
                
            if letter["Uppercase"] >= 1 and letter["Lowercase"] >= 1 and number >= 1 and special >= 1:
                return True
    return False


################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    result = 0
    for i in elements:
        result += i**2
        
    return result

# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    max_elmnt = 0
    for i in elements:
        if i > max_elmnt:
            max_elmnt = i
            
    return max_elmnt


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    duplicates = dict(zip(elements, [0]*len(elements)))
    removed = 0
    
    for i in range(len(elements)):
        duplicates[elements[i-removed]] += 1

        if elements[i-removed] in duplicates.keys() and duplicates[elements[i-removed]] > 1:
            elements.pop(i-removed)
            removed += 1
                
    return elements


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    result = []
    
    for index in range(len(elements)-1, -1, -1):
        result.append(elements[index])
        
    return result


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    result = []
    
    for item in elements:
        if isinstance(item, list):
            result += item
        else:
            result.append(item)
            
    return result



# Test funzioni
# print_test(sum_squares, [1, 2, 3])
# print_test(max_element, [1, 2, 3, -1, -2])
# print_test(remove_duplicates, [1, 2, 3, 2, 3])
# print_test(reverse_list, [1, 2, 3])
# print_test(flatten_list, [1, [2, 3]])

# Test funzioni
# print_test(make_hello, 'Pippo')
# print_test(strip_whitespace, '  Pippo  ')
# print_test(strip_whitespace, '   ')
# print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
# print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
# print_test(split_string, 'ciao, come, va, tutto, bene?  ', ', ')
# print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 't.', 'Hello')
# print_test(caesar_cypher, 'ciao pippo', 17, False)
# print_test(caesar_cypher, 'tzrf gzggf', 17, True)
# print_test(check_pwd, "a")
# print_test(check_pwd, "000000000000000000")
# print_test(check_pwd, "almeno6")
# print_test(check_pwd, "Aa@09asng2/")
# print_test(check_pwd, "Aa@09asng2")

et = time.time()
elapsed_time = et - st

print('Execution time:', elapsed_time, 'seconds')
