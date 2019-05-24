import random
lista_wyrzuc = []
lista_pytan = [["Jakiego koloru były smerfy?","A. niebieskiego", "B. różowego", "C. czerwony", "D. zielonego","A. niebieskiego", "A", "a"],
["Która z planet ma pierścienie?", "A. Pluton", "B. Saturn", "C. Neptun","D. Merkury", "B", "b"], 
["Jaka część mowy odpowiada na pytania: kto, co?", "A. przymiotnik", " B. czasownik", "C. rzeczownik", "D. przysłówek","C.rzeczownik", "C", "c"],
[" Kogo uratowała Calineczka?" " A. kreta", "B. jaskółkę", "D. pingwina" , "D. żabę","B. jaskółkę", "B", "b"]]
######################################################
def losowanie_nr_pytania(lista_pytan):
    return random.randint(0,len(lista_pytan)-1)
    

for i in range (0, 4):  #chwilowo jest w pętli - tylko by po calej liście pytań przeszło #jeśli każde pytanie z listy już wcześnie zostało zadane - idzie na nowe koło
    nr = losowanie_nr_pytania(lista_pytan)
    print(nr)
    for i in range(len(lista_wyrzuc)):
        if lista_pytan[nr] == lista_wyrzuc[i]:
            losowanie_nr_pytania(lista_pytan)
    
    print(lista_pytan[nr][0])  #printowanie pytania - z listy (używając wylocowany numer porządkowy)
    lista_wyrzuc.append(nr)
    print(lista_wyrzuc)
    for i in range(1, 5):     #printowanie 4!!! odpowiedzi do wyboru - z listy (używając wylocowany numer porządkowy)
        print(lista_pytan[nr][i], end = " ")
    print()
