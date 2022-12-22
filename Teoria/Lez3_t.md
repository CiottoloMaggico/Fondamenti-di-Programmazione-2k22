Slice params:

start = int()
end = int()

stringa[start:end]

step = int()

stringa[start:end:step]

Identico (python) -> stesso identico oggetto, si riferiscono entrambe allo stesso elemento
Uguali (python) -> in due spazi di memoria diversi è contenuta la stessa cosa

L'ottimizzazione viene applicata alle stringhe senza spazi e ai numeri piccoli

Gli attributi e i metodi che iniziano con "\_" sono privati e non vanno letti o modificati, solitamente

(\*\* = \_\_)

**eq** implementa l'operatore "=="
**add** implementa l'operatore "+"
**mul** implementa l'operatore "\*"
**len** implementa la funzione len

tutti gli oggetti che contengono questi metodi possono essere confrontati, addizionati, moltiplicati e ne può essere misurata la lunghezza

N = 3
N.**add**(5)

Namespaces: zone di memoria dove sono contenuti i nomi delle funzioni e delle variabili

variabili globali, funzioni globali sono accessibili in ogni parte del codice tuttavia sono altamente sconsigliate da utilizzare
variabili locali sono accessibili solo all'interno della funzione

il Garbage Collector ha il compito di ripulire tutti gli oggetti che non sono più raggiungibili dai programmi in esecuzione.
