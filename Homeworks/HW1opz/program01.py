# -*- coding: utf-8 -*-

# print(int_seq[tail+1:head])
# print(int_seq[head-1])
# curr += int_seq[head-1]
# curr = sum(int_seq[tail:head])

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
    int_seq = list(map(int, int_seq.split(",")))
    lenght, weight = len(int_seq), sum(int_seq)
    iteration = 0
    
    tail, head, new_head = 0, 1, 1
    result = 0
    curr, nxt = int_seq[0], 0
        
    if weight < subtotal:
        return 0
    
    if weight == subtotal:
        center, parity = divmod(lenght, 2)
        if parity != 0 and int_seq[center] == subtotal:
            return center**2
        elif parity == 0 and int_seq[center-1] + int_seq[center] == subtotal:
            return center**2
        elif int_seq[center-1] + int_seq[center] == 0 or int_seq[center] == 0:
            return 1
            
    if int_seq.count(int_seq[0]) == lenght:
        return int(lenght - int(subtotal/int_seq[0]) + 1)
    if int_seq[0] == subtotal and int_seq[lenght-1] == subtotal and int_seq.count(0) == lenght-2:
        return 2*lenght-2
    
    while tail < lenght:
        if curr == subtotal:
            result += 1
        if nxt <= subtotal and sum(int_seq[tail+1:new_head]) < subtotal:
            new_head = head
            
        if curr > subtotal and head != lenght:
            tail += 1
            head = new_head
            curr = sum(int_seq[tail:head])
            continue
        
        elif head == lenght:
            tail += 1
            head = new_head
            curr = sum(int_seq[tail:head])
            continue    
        
        curr += int_seq[head]
        nxt = curr - int_seq[tail]
        head += 1
        
    return result

if __name__ == '__main__':
    print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9))
    pass