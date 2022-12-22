Massimo valore gestibile da C/C++/Java/ecc: [0 -> (2^n)-1] - numeri negativi [-(2^n-1)-1 -> +(2^n-1)-1]
Python non ha limiti fissi nella gestione dei numeri, tuttavia dipende strettamente dalla capacità di memoria del calcolatore..

Codifica IEEE-754 viene usata per rappresentare i floating point
I floats sono approssimati utilizzando una parte dei 64 bit, per rappresentare le cifre (binarie) più significative moltiplicate per una potenza di 2

Segno | Mantissa | Esponente
1 bit 53 bit 10 bit

Mantissa inizia dal bit più significativo del numero (binario)
Esponente è una potenza di 2 che porta il bit più significativo a sx

- INTERI:
  Memoria variabile, garantiscono precisione teoricamente infinita
  Codificano solo operazioni con interi
