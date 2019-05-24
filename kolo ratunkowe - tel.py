import random
wylosowana_odpowiedz = random.choice("ABCD")
wylosowane_pytanie = random.randint(0,1)
lista_pytan = [
["Jakiego koloru były smerfy?","A. niebieskiego", "B. różowego", "C. czerwony", "D. zielonego","A. niebieskiego","A. niebieskiego", "A", "a"],
["Która z planet ma pierścienie?", "A. Pluton", "B. Saturn", "C. Neptun","D. Merkury","B. Saturn","B. Saturn", "B", "b"]
]
print(wylosowane_pytanie)

def telefon_do_przyjaciela(lista_pytan, wylosowane_pytanie):
    print("Hej, ziomek, gram teraz w Millijonerow. \nMam do Ciebie pytanie:", lista_pytan[wylosowane_pytanie][0], "\nCzy mozesz udzielic odpowiedzi?")
    print("Odpowiedz kolegi", wylosowana_odpowiedz)
    if wylosowana_odpowiedz == lista_pytan[wylosowane_pytanie][7]:
        print("I to dobra Odpowiedz")
    else:
        print("To zla odpowiedz :( ")

telefon_do_przyjaciela(lista_pytan,wylosowane_pytanie)
