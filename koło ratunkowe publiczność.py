import random
lista_pytan = [["Jakiego koloru były smerfy?","A. niebieskiego", "B. różowego", "C. czerwony", "D. zielonego","A. niebieskiego","A. niebieskiego", "A", "a"], ["Która z planet ma pierścienie?", "A. Pluton", "B. Saturn", "C. Neptun","D. Merkury","B. Saturn","B. Saturn", "B", "b"]]
numer_pytania=0
def kolo_publicznosc (lista_pytan, numer_pytania):
    licznik1=0
    licznik2=0
    licznik3=0
    licznik4=0
    for i in range(0,100):
        wylosowana=random.randint(1,100)  #losuje odpowiedzi publiczności
        if wylosowana>0 and wylosowana<=31:
            licznik1 +=1
        elif wylosowana >31 and wylosowana<=54:
            licznik2 +=1
        elif wylosowana>54 and wylosowana<=77:
            licznik3 +=1
        elif wylosowana>77:
            licznik4 +=1
    list= []        #robimy listę i dodajemy do niej wszystkie liczniki
    list.append(licznik1)
    list.append(licznik2)
    list.append(licznik3)
    list.append(licznik4)
    list.sort()    #sortujemy liczniki wg wielkości (od najmniejszego od największego)
    if lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][1]:       #spwawdzamy (po kolei) czy odpowiedzi od A do D są prawdziwe (porównujemy do prawdziwej odpowiedzi na miejscu 5 w liście)
        print("Publiczność zagłosowała na  odpowiedź ", lista_pytan[0][1], list[-1], "%", end = " ")  #jakby losowe przydzielenie wartości od odpowiedzi falszywych
        print ("Odpowiedź ", lista_pytan[0][2], "ma ", list[0], "% odpowiedź " ,lista_pytan[0][3], list[1],"% odpowiedź ", lista_pytan[0][4], list[2], "%")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][2]:
        print("Publiczność zagłosowała na odpowiedź ", lista_pytan[0][2], list[-1], "%", end = " ")
        print("Odpowiedź ", lista_pytan[0][1], list[0], "% odpowiedź ", lista_pytan[0][3], list[1], "% odpowiedź", lista_pytan[0][4], list[2], "%")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][3]:
        print ("Publiczność zagłosowała na odpowiedź ", lista_pytan[0][3], list[-1], "%", end = " ")
        print ("Odpowiedź ", lista_pytan[0][1], list[0], "% odpowiedź ", lista_pytan[0][2], list[1], "% odpowiedź", lista_pytan [0][4], list[2], "%")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][4]:
        print("Publiczność wybrała odpowiedź ", lista_pytan[0][4], list[-1], "%", end = " ")
        print ("Odpowiedź ", lista_pytan[0][1], list[0], "% odpowiedź ", lista_pytan[0][2], list[1], " % odpowiedź", lista_pytan [0][3], list[2], "%")
