import random
lista_pytan = [["Jakiego koloru były smerfy?","A. niebieskiego", "B. różowego", "C. czerwony", "D. zielonego","A. niebieskiego","A. niebieskiego", "A", "a"], ["Która z planet ma pierścienie?", "A. Pluton", "B. Saturn", "C. Neptun","D. Merkury","B. Saturn","B. Saturn", "B", "b"]] #-- USUNĄC POTEM
wylos_nr_pytania = 0    
##wyżej są chwilowe zmienne -- USUNĄC POTEM

def kolo_pol_na_pol(lista_pytan, wylos_nr_pytania):     #kolo przyjmuje z argumenty listę pytań i numer danego pytania wylosowanego przez komputer
    wylos_nr_2_odpowiedzi = random.randint(1, 4)        #pół na pół - jedna odp mrzawdziwa i jedna losowa -- w tym miejscu losujemy drugą możliwą odp
    while lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi] == lista_pytan[wylos_nr_pytania][5]:    #ta druga odpowiedź ma być inna niż prawdziwa
        wylosowanie_2_odpowiedzi = random.randint(1, 4)
    else:                 #jeśli druga możliwa odp jest różna od prawdziwej to ważna jest kolejność ich printowania, żeby nie było latwo (prawdziwa odp może być na początku czy na końcu)
        kolejnosc_wariantow = random.randint(1, 2)
        if kolejnosc_wariantow == 1:
            print(lista_pytan[wylos_nr_pytania][5], lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi]) #prawdziwa odp na początku
        else:
            print(lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi], lista_pytan[wylos_nr_pytania][5])  #prawdziwa odp na końcu
