#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uno dei meccanismi utilizzati per conservare e gestire grandi
quantità di dati è costituito dai database. Esistono tantissimi
tipi di database, ma quello che ha rivoluzionato il settore è
costituito dai database organizzati secondo il modello relazionale
teorizzato da Codd ormai mezzo secolo fa. Secondo questo modello
i dati sono organizzati in tabelle e relazioni fra di esse, in
modo da ottimizzare le richieste di memoria, favorire la coerenza
dei dati e minimizzare gli errori.

Dobbiamo progettare un insieme di funzioni che implementi una
semplice forma di database relazionale di una scuola di formazione
in cui ci sono quattro tabelle, ovvero students, teachers, courses
ed exams. I database sono di tre diverse dimensioni, ovvero small,
medium e large. Le tabelle del database di dimensione dbsize sono
salvate in quattro file json <dbsize>_<nometabella>.json (ad esempio,
il db small è composto dai file small_students.json, small_teachers.json,
small_courses.json e small_exams.json). Le tabelle sono organizzate in
liste di dizionari (si veda ad esempio small_students.json) e hanno le
seguenti strutture:
    - students: chiavi stud_code, stud_name, stud_surname, stud_email
    - teachers: chiavi teach_code, teach_name, teach_surname, teach_email
    - courses: chiavi course_code, course_name, teach_code
    - exams: chiavi exam_code, course_code, stud_code, date, grade.
La relazione fra le tabelle implica che ogni riga in ognuna delle
tabelle ha un riferimento ad un'altra tabella: ad esempio, un esame
(exam_code) corrisponde ad un voto (grade) dato da un docente
(teach_code) ad uno studente (stud_code) per aver sostanuto
l'esame di un certo corso (course_code) in una certa data (date). Ogni
studente può aver sostenuto diversi esami. Ogno docente può tenere
diversi corsi. Ogni corso è tenuto da un solo docente.

Il campo stud_code è una chiave primaria per la tabella students poiché
identifica univocamente uno studente, ovvero non esistono due studenti
con lo stesso stud_code. Similmente, teach_code, course_code ed exam_code
sono le chiavi primarie rispettivamente delle tabelle teachers, courses ed
exams. Per questo motivo, tali campi vengono utilizzati per realizzare
la relazione fra le tabelle.

Inoltre, i campi in tutte le tabelle non sono mai vuoti.

Dobbiamo realizzare alcune funzioni per poter interrogare i database delle
diverse dimensioni. Quindi, le funzioni prevedono di usare sempre il
parametro dbsize di tipo stringa, che può assumere i valori 'small',
'medium' e 'large'. Le funzioni sono:
    - media_studente(stud_code, dbsize), che riceve una stud_code di
      uno studente e ritorna la media dei voti degli esami sostenuti,
      dallo studente.
    - media_corso(course_code, dbsize), che riceve un identificatore per un
      corso e ritorna la media dei voti degli esami per quel corso,
      sostenuti da tutti gli studenti.
    - media_docente(teach_code, dbsize), che riceve un identificatore
      di un docente e ritorna la media dei voti per gli esami
      sostenuti in tutti i corsi del docente.
    - studenti_brillanti(dbisze), che ritorna la lista delle matricole
      (stud_code) con una media di esami sostenuti superiore o uguale a 28,
      ordinate in modo decrescente per media e, in caso di parità, in
      ordine lessicografico per il cognome e il nome dello studente. In
      caso di ulteriore parità, si usi il valore numerico dello stud_code
      in ordine crescente.
    - stampa_esami_sostenuti(stud_code, fileout, dbsize), che riceve un
      numero di stud_code e salva nel file fileout la lista degli esami
      sostenuti dallo studente identificato dal valore stud_code.
      Le righe nel file devono essere ordinate in modo crescente
      per data di esame sostenuto e, in caso di stessa data, in ordine
      alfabetico. Il file ha una riga iniziale con il testo
       "Esami sostenuti dallo studente  <stud_surname> <stud_name>, matricola <stud_code>",
      mentre le righe seguenti hanno la seguente struttura
        "<course_name>\t<date>\t<grade>", in cui i campi sono allineati
      rispetto al nome del corso più lungo (ovvero tutte le date e
      i voti sono allineati verticalmente). La funzione ritorna
      il numero di esami sostenuti dallo studente.
    - stampa_studenti_brillanti(fileout, dbsize), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.
    - stampa_verbale(exam_code, fileout, dbsize), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

Tutte le medie devono essere arrotondate alla seconda cifra decimale,
anche prima di ogni funzione di ordinamento.
Tutti i file devono avere encoding "utf8".
Per stampare agevolmente righe allineate considerare la funzione format con
i modificatori per l'allineamento (https://pyformat.info/#string_pad_align)
e con i parametri dinamici (https://pyformat.info/#param_align).
"""
import json


def json_opener(function, dbsize):
    return json.load(open(f"{dbsize}_{function}.json", "r", encoding="utf8"))


def top_students_custom(dbsize):
    exams = json_opener("exams", dbsize)
    names = json_opener("students", dbsize)
    students = {}
    for exam in exams:
        students[exam["stud_code"]] = students.get(
            exam["stud_code"], []) + [exam["grade"]]
    top_students = dict([x for x in map(lambda x: (x[0], (sum(x[1]))/len(x[1])) if sum(
        x[1])/len(x[1]) >= 28 else None, students.items()) if x != None])
    top_student_final = []
    for student in names:
        if student["stud_code"] in top_students:
            top_student_final += (float('%.2f' % top_students[student["stud_code"]]), student['stud_surname'], student['stud_name'], student["stud_code"]),
    return top_student_final


def media_studente(stud_code, dbsize):
    grades = tuple(map(lambda x: x["grade"], filter(
        lambda x: x["stud_code"] == stud_code, json_opener("exams", dbsize))))
    return float('%.2f' % (sum(grades)/len(grades)))


def media_corso(course_code, dbsize):
    grades = tuple(map(lambda x: x["grade"], filter(
        lambda x: x["course_code"] == course_code, json_opener("exams", dbsize))))
    return float('%.2f' % (sum(grades)/len(grades)))


def media_docente(teach_code, dbsize):
    courses = tuple(map(lambda x: x["course_code"], filter(
        lambda x: x["teach_code"] == teach_code, json_opener("courses", dbsize))))

    grades = [entry["grade"] for entry in json_opener(
        "exams", dbsize) if entry["course_code"] in courses]
    return float('%.2f' % (sum(grades)/len(grades)))


def studenti_brillanti(dbsize):
    full_view = top_students_custom(dbsize)
    full_view.sort(key=lambda x: (-x[0], f"{x[1]}{x[2]}", x[3]))
    top_stud = [x[3] for x in full_view]
    return top_stud

def stampa_verbale(exam_code, dbsize, fileout):
    exams, students, courses, teachers = json_opener('exams', dbsize), json_opener(
        'students', dbsize), json_opener('courses', dbsize), json_opener('teachers', dbsize)

    for exam in exams:
        if exam['exam_code'] == exam_code:
            start = exam
            break
    for student in students:
        if student['stud_code'] == start['stud_code']:
            stud_name, stud_surname = student['stud_name'], student['stud_surname']
            break
    for course in courses:
        if course['course_code'] == start['course_code']:
            course_name, teach_code = course['course_name'], course['teach_code']
            break
    for teacher in teachers:
        if teacher['teach_code'] == teach_code:
            teach_name, teach_surname = teacher['teach_name'], teacher['teach_surname']
    with open(fileout, "w", encoding="utf8") as file:
        file.write(
            f"Lo studente {stud_name} {stud_surname}, matricola {start['stud_code']}, ha sostenuto in data {start['date']} l'esame di {course_name} con il docente {teach_name} {teach_surname} con votazione {start['grade']}.")
        file.close()
    return start['grade']


def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    stud_infos = tuple(filter(lambda x: x['stud_code'] ==
                              stud_code, json_opener('students', dbsize)))[0]
    stud_exams = list(filter(lambda x: x['stud_code'] ==
                             stud_code, json_opener('exams', dbsize)))
    courses = dict([(x['course_code'], x['course_name']) for x in json_opener(
        'courses', dbsize)])

    header = [
        f"Esami sostenuti dallo studente {stud_infos['stud_surname']} {stud_infos['stud_name']}, matricola {stud_code}\n"
    ]
    body = [
        [courses[x['course_code']], x['date'], str(x['grade'])] for x in stud_exams
    ]
    max_len = len(max(body, key=lambda x: len(x[0]))[0])
    body.sort(key=lambda x: (x[1], x[0]))
    header.extend(
        [f"{line[0]}{' '*(max_len-len(line[0]))}\t{line[1]}\t{line[2]}\n" for line in body])

    with open(fileout, "w", encoding="utf8") as file:
        file.writelines(header)
        file.close()

    return len(stud_exams)


def stampa_studenti_brillanti(dbsize, fileout):
    top_stud = sorted(top_students_custom(dbsize), key=lambda stud: (-stud[0], f"{stud[1]}{stud[2]}"))
    stud_max = max(top_stud, key=lambda x: len(f'{x[1]}{x[2]}'))
    max_len = len(f'{stud_max[1]}{stud_max[2]}')
    file_formatted = [
        f"{stud[1]} {stud[2]}{' '*(max_len-len(f'{stud[1]}{stud[2]}'))}\t{stud[0]}\n" for stud in top_stud]

    with open(fileout, "w") as file:
        file.writelines(file_formatted)

    return len(top_stud)


if "__main__" == __name__:
    pass