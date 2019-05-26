
import random
import time
import os
import sys
from colorama import init, Style
from termcolor import colored
init()
######################################################
lista_pytan = [
["Jakiego koloru były smerfy?", "A. niebieskiego", "B. różowego", "C. czerwony", "D. zielonego","A. niebieskiego", "A", "a"],
["Która z planet ma pierścienie?", "A. Pluton", "B. Saturn", "C. Neptun", "D. Merkury", "B. Saturn", "B", "b"],
["Jaka część mowy odpowiada na pytania: kto, co?", "A. przymiotnik", " B. czasownik", "C. rzeczownik", "D. przysłówek","C.rzeczownik", "C", "c"],
["Kogo uratowała Calineczka?", "A. kreta", "B. jaskółkę", "D. pingwina" , "D. żabę", "B. jaskółkę", "B", "b"],
["Jaka legenda jest związana z Warszawą?", "A. o smoku wawelskim", "B. o Popielu", "C. o Wandzie, co nie chciała Niemca", "D. o syrence", "D. o syrence", "D", "d"],
["Kto ma łeb obdarty?", "A. kto późno przychodzi", "B. kto jest krótko ostrzyżony", "C. kto gra w karty", "D. kto ma nos zadarty", "C. kto gra w karty", "C", "c"],
["Co nie jest nazwą stylu pływackiego?", "A. rekin", "B. kraul", "C. żabka", "D. delfin", "A.rekin", "A", "a"],
["Która z tych małp jest największa?", "A. orangutan",  "B. kapucynka", "C. szympans", "D. goryl", "D. goryl", "D", "d"],
["W jakim mieście jest Wawel?", "A. we Wrocławiu",  "B. w Warszawie", "C. w Poznaniu", "D. w Krakowie", "D. w Krakowie", "D", "d"],
["Do ilu punktów liczy się set w tenisie stołowym?", "A. 21", "B. 25","C. 31", "D. 20", "A. 21", "A", "a"],
["Jakie są najwyższe góry na świecie?", "A. Tatry," ,"B. Himalaje", "C. Pireneje", "D. Alpy", "B. Himalaje", "B", "b"],
["Gdzie leży Arktyka?", "A. wokół bieguna południowego", "B. wokół bieguna północnego", "C. na równiku", "D. na Księżycu", "B. wokół bieguna północnego", "B", "b"],
["Która szkoła wyższa jest najstarsza w Polsce?", "A. Szkoła Główna Handlowa", "B. Akademia Górniczo-Hutnicza", "C. Uniwersytet Jagielloński", "D. Uniwersytet Warszawski", "C. Uniwersytet Jagielloński", "C", "c"],
["Który z podanych prezydentów Polski sprawował urząd najdłużej?", "A. Lech Wałęsa", "B. Aleksander Kwaśniewski", "C. Lech Kaczyński", "D. Bronisław Komorowski", "B. Aleksander Kwaśniewski", "B", "b"],
["W którym roku Słowacja wprowadziła walutę euro?", "A. w 2010", "B. w 2012", "C. w 2009", "D. w 2007", "C. w 2009", "C", "c"],
["Międzynarodowa organizacja policyjna ścigająca przestępstwa kryminalne to:", "A. Mosad", "B. Czeka", "C. Interpol", "D. Secret Service", "C. Interpol", "C", "c"],
["Kopa to", "A. 10 sztuk", "B. 12 sztuk", "C. 50 sztuk", "D. 60 sztuk", "D. 60 sztuk", "D", "d"],
["Morze Martwe znane jest z następującego związku chemicznego:", "A. NaCl", "B. HCl", "C. H20", "D. NaOH", "A. NaCl", "A", "a"],
["Które z określeń nie oznacza wysłannika?", "A. emisariusz", "B. kurier", "C. poseł", "D. ordynat", "D. ordynat", "D", "d"],
["Jakie włoskie miasto było tłem romansu Romea i Julii?", "A. Werona", "B. Wenecja", "C. Florencja", "D. Palermo", "A. Werona", "A", "a"]
]
######################################################
lista_progow = ["500","1 000","2 000","5 000","10 000","20 000","40 000","75 000","125 000","250 000","500 000","1 000 000","0"]
wskaznik_progu = 0
wskaznik_progu_gw = 0
######################################################
przegrana = 0
rezygnacja = 0
telefon_został_wykorzystany = 0
pytdopub_został_wykorzystany = 0
polnapol_został_wykorzystany = 0
###################################################################################################################
###################################################################################################################
###################################################################################################################
#funkcja ktora wyswietla sie na poczatku programu, przed pytaniami
def powitanie():
    print("Witaj! Mam na imię Ubert Hurbański i dziś zagrasz o milion złotych!\n")
###################################################################################################################
def telefon_do_przyjaciela(lista_pytan, wylosowane_pytanie):
    global wskaznik_progu
    print("Dzwonimy do przyjaciela.")
    for i in range(0,3):
        print("*",end='')
        time.sleep(1.2)
    print("\nLukasz Morawiecki, słucham?")
    time.sleep(2)
    print("Hej, Lukaszu, gram teraz w Millionerów. \nMam do Ciebie pytanie:", lista_pytan[wylosowane_pytanie][0])
    time.sleep(2)
    print("Czy możesz udzielić odpowiedzi?")
    tablica_dla_los = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"]   #LISTA Z KTÓREJ LOSUJEMY ODPOWIEDŻ KOLEGI
    for i in range(0,13-wskaznik_progu+random.randint(-1,3)): #zwiększamy w tym miejscu prawdopodobieństwo wylosowania prawidłowej odp
        tablica_dla_los.append(lista_pytan[wylosowane_pytanie][6])
    wylosowana_odpowiedz = random.choice(tablica_dla_los)#losuje nam odpowiedzi od abcd - im wyzszy numer pytania tym mniejsza szansa na poprawna odp
    for i in range(0,3):
        print("*",end='')
        time.sleep(1.2)
    print("\nPanie Lukaszu, czy Pan juz moze podać odpowiedź?")
    time.sleep(1)
    print("Odpowiedź kolegi:", wylosowana_odpowiedz)

##########################################################################################################################
def kolo_pol_na_pol(lista_pytan, wylos_nr_pytania):     #kolo przyjmuje z argumenty listę pytań i numer danego pytania wylosowanego przez komputer
    wylos_nr_2_odpowiedzi = random.randint(1, 4)        #pół na pół - jedna odp mrzawdziwa i jedna losowa -- w tym miejscu losujemy drugą możliwą odp
    while lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi] == lista_pytan[wylos_nr_pytania][5]:    #ta druga odpowiedź ma być inna niż prawdziwa
        wylosowanie_2_odpowiedzi = random.randint(1, 4)
    else:                 #jeśli druga możliwa odp jest różna od prawdziwej to ważna jest kolejność ich printowania, żeby nie było latwo (prawdziwa odp może być na początku czy na końcu)
        kolejnosc_wariantow = random.randint(1, 2)
        if kolejnosc_wariantow == 1:
            print(lista_pytan[wylos_nr_pytania][5], " ", lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi]) #prawdziwa odp na początku
        else:
            print(lista_pytan[wylos_nr_pytania][wylos_nr_2_odpowiedzi], " ", lista_pytan[wylos_nr_pytania][5])  #prawdziwa odp na końcu
###############################################################################################################################
def publicznosc (lista_pytan, numer_pytania): ####################koło publicznosc
    licznik1=0
    licznik2=0
    licznik3=0
    licznik4=0
    for i in range(0,100):
        wylosowana=random.randint(1,100)
        if wylosowana>0 and wylosowana<=31:
            licznik1 +=1
        elif wylosowana >31 and wylosowana<=54:
            licznik2 +=1
        elif wylosowana>54 and wylosowana<=77:
            licznik3 +=1
        elif wylosowana>77:
            licznik4 +=1
    list= []
    list.append(licznik1)
    list.append(licznik2)
    list.append(licznik3)
    list.append(licznik4)
    list.sort()
    if lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][1]:
        print ("Publiczność zagłosowała na  odpowiedź", lista_pytan[numer_pytania][1],"-", list[-1], "%.")
        print ("odpowiedź", lista_pytan[numer_pytania][2], "-", list[0], "%;  odpowiedź" ,lista_pytan[numer_pytania][3], "-", list[1],"%;  odpowiedź", lista_pytan[numer_pytania][4], "-", list[2], "%;")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][2]:
        print ("Publiczność zagłosowała na odpowiedź", lista_pytan[numer_pytania][2],"-", list[-1], "%.")
        print ("odpowiedź", lista_pytan[numer_pytania][1], "-", list[0], "%;  odpowiedź", lista_pytan[numer_pytania][3], "-", list[1], "%;  odpowiedź", lista_pytan[numer_pytania][4], "-", list[2], "%;")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][3]:
        print ("Publiczność zagłosowała na odpowiedź", lista_pytan[numer_pytania][3],"-", list[-1], "%.")
        print ("odpowiedź", lista_pytan[numer_pytania][1], "-", list[0], "%;  odpowiedź", lista_pytan[numer_pytania][2], "-", list[1], "%;  odpowiedź", lista_pytan [numer_pytania][4], "-", list[2], "%;")
    elif lista_pytan[numer_pytania][5]== lista_pytan[numer_pytania][4]:
        print ("Publiczność wybrała odpowiedź", lista_pytan[numer_pytania][4], "-", list[-1], "%.")
        print ("odpowiedź", lista_pytan[numer_pytania][1], "-", list[0], "%;  odpowiedź", lista_pytan[numer_pytania][2], "-", list[1], "%;  odpowiedź", lista_pytan [numer_pytania][3], "-", list[2], "%;")
###########################################################################3
def generacja_kolejnosci_pytan(size = 10):
    lista = []
    for i in range(0, size):
        lista.append(i)
    for i in range(0, size):
        rnd1 = random.randint(0, size - 1)
        rnd2 = random.randint(0, size - 1)
        lista[rnd1], lista[rnd2] = lista[rnd2], lista[rnd1]
    return (lista)

def wyswietlanie_pytania(lista_pytan, numer_pytania):
    wyswietl_prog(lista_progow)
    print("")
    print(lista_pytan[numer_pytania][0])  #printowanie pytania - z listy (używając wylocowany numer porządkowy)
    for i in range(1, 5):     #printowanie 4!!! odpowiedzi do wyboru - z listy (używając wylocowany numer porządkowy)
        if i==3:
            print("")
        print(lista_pytan[numer_pytania][i], end = "   ")
###################################################################################################################
def przyjmowanie_odp(lista_pytan,numer_pytania):
    global przegrana
    global rezygnacja
    global wskaznik_progu
    global wskaznik_progu_gw
    while True:
        print("\n")
        wybor_uzytkownika = input("Koła ratunkowe: 1 - telefon do przyjaciela; 2 - pol na pol; 3 - pytanie do publicznosci.\nPS.dla rezygnacji wciśnij \"X\".\nCo wybierasz?\n")  #wpisywanie odpowiedzi #jak poprosic o wpisanie "A" czy "a"?
        if wybor_uzytkownika == lista_pytan[numer_pytania][6] or wybor_uzytkownika == lista_pytan[numer_pytania][7]:   #sprawdzanie czy wpisana odpowiedz prawdziwa; MA BYĆ NA 6 i 7 MIEJSCU PORZĄDKOWYM(DLA KOMPUTERA NA 5 i 6) W LIŚCIE!! #są dwa możliwe warianty wpisania "A" czy "a" - dlatego robimy (żeby nie przekształcać potem input) odrazu możliwość "A" czy "a".
            print("Brawo, to poprawna odpowiedź!")
            wskaznik_progu += 1
            if wskaznik_progu!=2 or wskaznik_progu!=7:
                pass
            if wskaznik_progu==2:
                wskaznik_progu_gw=1000
            if wskaznik_progu==7:
                wskaznik_progu_gw=40000
            for i in range(3,0,-1): #odlicza 321 po prawidlowej odpowiedzi, end="\r" znaczy ze nadpisuje aktualną linijkę, dlatego licznik wyswietla sie ladnie w jednym miejscu
                print(i,end="\r")
                time.sleep(0.4)
            os.system('cls')
            break
        elif wybor_uzytkownika == '1':
            global telefon_został_wykorzystany
            if telefon_został_wykorzystany == 0:
                telefon_do_przyjaciela(lista_pytan,numer_pytania)
                telefon_został_wykorzystany = 1
            else:
                print("Już wykorzystałeś/aś koło ratunkowe \"Telefon\" jeden raz - więcej nie wolno")
        elif wybor_uzytkownika =='2':
            global polnapol_został_wykorzystany
            if polnapol_został_wykorzystany == 0:
                kolo_pol_na_pol(lista_pytan,numer_pytania)
                polnapol_został_wykorzystany = 1
            else:
                print("Już wykorzystałeś/aś koło ratunkowe \"Pół na pół\" jeden raz - więcej nie wolno")
        elif wybor_uzytkownika =='3':
            global pytdopub_został_wykorzystany
            if pytdopub_został_wykorzystany == 0:
                publicznosc(lista_pytan,numer_pytania)
                pytdopub_został_wykorzystany = 1
            else:
                print("Już wykorzystałeś/aś koło ratunkowe \"Pytanie do publiczności\" jeden raz - więcej nie wolno")
        elif wybor_uzytkownika =='X' or wybor_uzytkownika=='x':
            rezygnacja=1
            break
        elif not wybor_uzytkownika in "ABCD123Xabcdx" or wybor_uzytkownika=="": #jeśli gracz wpisał inny znak niż dozwolone, napisz mu że zły klawisz
            print("Niepoprawna komenda, spróbuj ponownie.")
        else:
            przegrana=1
            break
###################################################################################################################
def wyswietl_prog(lista_progow): #wyswietla progi i do kazdego dodaje kilka spacji po to zeby bylo wysrodkowane; podswietla progi gwarantowane; podswietla kase za aktualne pytanie
    #ta funkcja ma trzy opcje:
    #  - jeśli zostanie wywołana podczas gry, wtedy wyświetla listę progów i podświetla aktualne pytanie
    #  - jeśli zostanie wywołana po przegranej, wtedy wyświetła całą listę progów na czerwono
    #  - jeśli zostanie wywołana po rezygnacji lub gdy się wygra, wtedy wyświetla listę progów i podświetla na zielono ile zabraliśmy do domu
    global wskaznik_progu
    global wskaznik_progu_gw
    print(" MILIONERZY\n")
    if przegrana==1:
        print(" ",end='')
        print(colored("1 000 000",'red','on_white'))
        print(colored("  500 000",'red'))
        print(colored("  250 000",'red'))
        print(colored("  125 000",'red'))
        print(colored("   75 000",'red'))
        print("   ",end='')
        print(colored("40 000",'red','on_white'))
        print(colored("   20 000",'red'))
        print(colored("   10 000",'red'))
        print(colored("    5 000",'red'))
        print(colored("    2 000",'red'))
        print("    ",end='')
        print(colored("1 000",'red','on_white'))
        print(colored("      500",'red'))
    elif rezygnacja==1 or wskaznik_progu==12:
        wskaznik_progu-=1
        if wskaznik_progu==11:
            print(" ",end='')
            print(colored("1 000 000",'white','on_green'))
        else:
            print(" ",end='')
            print(colored("1 000 000",'grey','on_white'))
        if wskaznik_progu==10:
            print(colored("  500 000",'white','on_green'))
        else:
            print("  500 000")
        if wskaznik_progu==9:
            print(colored("  250 000",'white','on_green'))
        else:
            print("  250 000")
        if wskaznik_progu==8:
            print(colored("  125 000",'white','on_green'))
        else:
            print("  125 000")
        if wskaznik_progu==7:
            print(colored("   75 000",'white','on_green'))
        else:
            print("   75 000")
        if wskaznik_progu==6:
            print("   ",end='')
            print(colored("40 000",'white','on_green'))
        else:
            print("   ",end='')
            print(colored("40 000",'grey','on_white'))
        if wskaznik_progu==5:
            print(colored("   20 000",'white','on_green'))
        else:
            print("   20 000")
        if wskaznik_progu==4:
            print(colored("   10 000",'white','on_green'))
        else:
            print("   10 000")
        if wskaznik_progu==3:
            print(colored("    5 000",'white','on_green'))
        else:
            print("    5 000")
        if wskaznik_progu==2:
            print(colored("    2 000",'white','on_green'))
        else:
            print("    2 000")
        if wskaznik_progu==1:
            print("    ",end='')
            print(colored("1 000",'white','on_green'))
        else:
            print("    ",end='')
            print(colored("1 000",'grey','on_white'))
        if wskaznik_progu==0:
            print(colored("      500",'white','on_green'))
        else:
            print("      500")
    else:
        if wskaznik_progu==11:
            print(" ",end='')
            print(colored("1 000 000",'cyan','on_white'))
        else:
            print(" ",end='')
            print(colored("1 000 000",'grey','on_white'))
        if wskaznik_progu==10:
            print(colored("  500 000",'cyan'))
        else:
            print("  500 000")
        if wskaznik_progu==9:
            print(colored("  250 000",'cyan'))
        else:
            print("  250 000")
        if wskaznik_progu==8:
            print(colored("  125 000",'cyan'))
        else:
            print("  125 000")
        if wskaznik_progu==7:
            print(colored("   75 000",'cyan'))
        else:
            print("   75 000")
        if wskaznik_progu==6:
            print("   ",end='')
            print(colored("40 000",'cyan','on_white'))
        else:
            print("   ",end='')
            print(colored("40 000",'grey','on_white'))
        if wskaznik_progu==5:
            print(colored("   20 000",'cyan'))
        else:
            print("   20 000")
        if wskaznik_progu==4:
            print(colored("   10 000",'cyan'))
        else:
            print("   10 000")
        if wskaznik_progu==3:
            print(colored("    5 000",'cyan'))
        else:
            print("    5 000")
        if wskaznik_progu==2:
            print(colored("    2 000",'cyan'))
        else:
            print("    2 000")
        if wskaznik_progu==1:
            print("    ",end='')
            print(colored("1 000",'cyan','on_white'))
        else:
            print("    ",end='')
            print(colored("1 000",'grey','on_white'))
        if wskaznik_progu==0:
            print(colored("      500",'cyan'))
        else:
            print("      500")
###################################################################################################################
###################################################################################################################
###################################################################################################################

#START OF THE GAME
powitanie()

rozmiar_listy = len(lista_pytan)
kolejnosc_pytan = generacja_kolejnosci_pytan(rozmiar_listy)

obecny = 0

#MAIN LOOP OF THE GAME
while True:
    if wskaznik_progu==12: #jeśli gracz odpowiedzial na ostatnie pytanie, wyswietl ze wygral milion i zakoncz program
        wyswietl_prog(lista_progow)
        print("Brawo, to prawidłowa odpowiedź na ostatnie pytanie!")
        print("Wygrałeś MILION ZŁOTYCH!")
        break
    if przegrana==0 and rezygnacja==0: #jesli przegrana rowna sie zero (czyli nie przegral), wyswietl kolejne pytanie
        aktualne_pytanie=kolejnosc_pytan[obecny]
        obecny += 1
        wyswietlanie_pytania(lista_pytan,aktualne_pytanie)
        przyjmowanie_odp(lista_pytan,aktualne_pytanie)
    else: #jesli przegrana rowna sie jeden (czyli jesli przegral) lub rezygnacja rowna sie jeden (czyli jesli zrezygnowal) to wyswietl stosowny komunikat i zakoncz program
        if przegrana==1:
            os.system('cls')
            wyswietl_prog(lista_progow)
            print("\nBardzo mi przykro, przegrałeś grę! Odchodzisz z kwotą:",wskaznik_progu_gw)
            break
        elif rezygnacja==1:
            os.system('cls')
            wyswietl_prog(lista_progow)
            print("Zrezygnowałeś z dalszej gry. Odchodzisz z kwotą:",lista_progow[wskaznik_progu])
            break
