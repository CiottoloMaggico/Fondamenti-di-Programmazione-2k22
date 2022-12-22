# Ignorare le righe fino alla 35
from re import X
from typing import Any, Callable, List, Tuple
import sys
from unittest import result


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


# Scrivere una funzione che converte una stringa di caratteri numerici
# nell'intero corrispondente. Non usare la funzione `int(string)`.
def string_to_int(string: str) -> int:
    number = 0
    for character in string:
        number = number * 10 + ord(character) - ord('0')
        
    return number


# Scrivere una funzione che converte un intero in una stringa di caratteri
# numerici corrispondenti all'intero. Non usare la funzione `str(integer)`.
def int_to_string(integer: int) -> str:
    string = ""
    while integer > 0:
        string = chr(integer % 10 + ord('0')) + string
        integer = integer // 10
    return string


# Scrivere una funzione che data una stringa, ritorna una lista di tuple
# consituita da parola e frequenza, ordinata per frequenza. La frequenza è
# il numero di volte in cui la parole appare nel testo.
# Per evitare problemi nel trovare le parole, togliere tutti i caratteri
# non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo.
# Usare la funzione `isalnum()` per testare i caratteri.
def word_frequency(string: str) -> List[Tuple[str, int]]:
    string = string.lower().split()
    res = {}
    
    for item in string:
        for word in range(len(item)):
            if not item[word].isalnum() or word == len(item)-1:
                if word == len(item)-1 and item[word].isalnum():
                    word += 1
                if item[:word] in res:
                    res[item[:word]] += 1
                else:
                    res[item[:word]] = 1
                    
    res = sorted(list(zip(res.values(), res.keys())), key=lambda x: x[0]) 
                    
    return res

# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str) -> int:
    result = {}
    string = string.split()

    for num in string:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    
    new_result = sorted([int(x[0]) for x in list(filter(lambda x: x[1] == max(result.values()), result.items()))])
    return new_result


# Implementare una funzione *ricorsiva* che data una lista contenente valori
# e sottoliste, ritorna una lista contenente tutti i valori. Ad esempio:
# [1, [2, 3]] => [1, 2, 3] e [1, [2, [3, 4]]] => [1, 2, 3, 4]
def flatten_list(elements: list) -> list:
    res = []
    
    for element in elements:
        if type(element) is list:
            res += flatten_list(element)
        else:
            res += [element]
    
    return res


# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    result = {}
    
    for dicti in dictionaries:
        for key, value in dicti.items():
            if key in result and value > result[key]:
                result[key] = value
            else:
                result[key] = value
                
    return result

# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei due di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    result = {}
    
    for dicti in dictionaries:
        for key, value in dicti.items():
            if key in result and value not in result[key]:
                result[key] += [value]
            elif key not in result:
                result[key] = [value]
                
    return result


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    common_keys = list(list(dictionaries[i-1].keys() & dictionaries[i].keys() for i in range(1, len(dictionaries)))[0])
    result = dict([(key, []) for key in common_keys])
    
    for index in range(len(dictionaries)):
        for key, value in dictionaries[index].items():
            if key in result:
                result[key] += [value]
        
    return result


# Test funzioni
# check_test(string_to_int, 5, "5")
# check_test(string_to_int, 123, "123")
# check_test(int_to_string, "5", 5)
# check_test(int_to_string, "123", 123)
# check_test(word_frequency, [(1, "ciao"), (1, "pippo")], "Ciao Pippo")
# check_test(word_frequency, [(1, "pluto"), (2, "pippo")], "Pippo Pluto Pippo")
# check_test(word_frequency, [(1, 'pippo'), (1, 'pluto'),
#            (2, 'ciao')], "Ciao Pippo! Ciao Pluto!")
# check_test(number_frequency, [10], "1 2 2 3 10 10 10")
# check_test(number_frequency, [2, 5], "1 1 5 5 5 2 2 2")
# check_test(flatten_list, [1, 2, 3], [1, [2, 3]])
# check_test(flatten_list, [1, 2, 3, 4], [1, [2, [3, 4]]])
# check_test(flatten_list, [1, 2, 3, 4, 5, 6, 7, 8],
#            [1, [2, [3, 4], 5, [6, [7, 8]]]])
# check_test(update_dict, {'Ciao': 1, 'Pippo': 2, 'Pluto': 3},
#            [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
# check_test(update_dict, {'Ciao': 1, 'Pippo': 4, 'Pluto': 3}, [{
#            "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
# check_test(merge_dict, {'Ciao': [1], 'Pippo': [2], 'Pluto': [3]},
#            [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
# check_test(merge_dict, {'Ciao': [1], 'Pippo': [2, 4], 'Pluto': [3]}, [{
#            "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
# check_test(intersect_dict, {'Pippo': [2, 3]},
#            [{"Ciao": 1, "Pippo": 2}, {"Pippo": 3, "Pluto": 4}])
# check_test(intersect_dict, {'Pippo': [2, 3], 'Pluto': [5, 4]},
#            [{"Ciao": 1, "Pippo": 2, "Pluto": 5}, {"Pippo": 3, "Pluto": 4}])