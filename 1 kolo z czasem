def telefon_do_przyjaciela(lista_pytan, wylosowane_pytanie):
    for i in range(0,10):
        print("*")
        time.sleep(2)
    print("Lukasz Morawiecki, slucham")

    print("Hej, Lukaszu, gram teraz w Millijonerów. \n Mam do Ciebie pytanie:", lista_pytan[wylosowane_pytanie][0], "\nCzy mozesz udzielic odpowiedzi?")
    tablica_dla_los = ["A", "B", "C", "D"]   #LISTA Z KTÓREJ LOSUJEMY ODPOWIEDŻ KOLEGI
    tablica_dla_los.append(lista_pytan[wylosowane_pytanie][6]) #zwiększamy w tym miejscu prawdopodobieństwo wylosowania prawidłowej odp
    tablica_dla_los.append(lista_pytan[wylosowane_pytanie][6])
    wylosowana_odpowiedz = random.choice(tablica_dla_los)
     #losuje nam odpowiedzi od abcd +2literki
     time.sleep(10)
     print("Panie Lukaszu, czy Pan juz moze podac odpowiedz?")
    print("Odpowiedz kolegi:", wylosowana_odpowiedz)
telefon_do_przyjaciela(lista_pytan,numer_pytania)
