# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from test_01 import Test" "Test.main()"

"""
Consideriamo la codifica dei numeri romani e la modifica suggerita da 
Randall Munroe nel suo blog XKCD.
Nella codifica dei numeri romani:
- non esiste lo zero
- si usano le lettere 'IVXLCDM' che corrispondono ai valori decimali
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- i numeri si scrivono da sinistra a destra cominciando con i valori più alti 
  (migliaia, centinaia, decine, unità)
- i valori delle lettere si sommano, tranne quando sono seguiti da lettere di peso maggiore, 
  nel qual caso si sottraggono
- si possono usare al massimo 3 lettere consecutive uguali per le lettere 'IXCM'
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- per rappresentare i valori che hanno cifra decimale 4 o 9 si usa la sottrazione 
  dalla lettera seguente
  Es. 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

Nel suo blog XKCD, invece, Randall Munroe codifica i numeri romani con i corrispondenti numeri arabi: 
si concatenano i numeri arabi ottenuti sostituendo a ciascuna lettera il valore corrispondente.  
Es.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Chiamiamo questa codifica "formato XKCD".

Obiettivo dello homework è decodificare una lista di stringhe che rappresentano
numeri romani nel formato XKCD, e tornare i K valori maggiori in ordine decrescente.

Implementate quindi le seguenti funzioni:
"""


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    '''
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    '''
    if 0 < k <= len(xkcd_values):
        return list(sorted(map(decode_value, xkcd_values), reverse=True))[:k]


def decode_value(xkcd: str) -> int:
    '''
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente

    Esempio: '10010010010100511' -> 397
    '''
    weights = tuple(map(int, "".join([xkcd[i-1] if xkcd[i] == "0" else (
        xkcd[i-1]+"|") for i in range(1, len(xkcd))]+[xkcd[-1]]).split("|")))
    return sum((-weights[i] if weights[i] < weights[i+1] else weights[i] for i in range(len(weights)-1)))+weights[-1]


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    '''
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    Esempio: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    return list(map(int, "".join([xkcd[i-1] if xkcd[i] == "0" else (
        xkcd[i-1]+"|") for i in range(1, len(xkcd))]+[xkcd[-1]]).split("|")))


def list_of_weights_to_number(weigths: list[int]) -> int:
    '''
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante

    Esempio: [100, 100, 100, 10, 100, 5, 1, 1] -> 397
    '''
    weigths = tuple(weigths)
    return sum((-weigths[i] if weigths[i] < weigths[i+1] else weigths[i] for i in range(len(weigths)-1)))+weigths[-1]


###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print(decode_value("10010010010100511"))
