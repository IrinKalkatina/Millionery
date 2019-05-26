
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

def reklama():
    global wskaznik_progu
    teksty_reklama_c=[
    "Ubert Hurbański: Odpowiedź poznamy po przerwie.",
    "Ubert Hurbański: Czas na reklamę. ",
    "Ubert Hurbański: Wracamy po przerwie, bądźcie Państwo z nami.",
    "Ubert Hurbański: Dowiemy się zaraz po przerwie.",
    ]
    teksty_reklama_m=[
    "Ubert Hurbański: Powiem ci coś, co ci się nie spodoba",
    "Ubert Hurbański: Nie sądzę, że będziesz zadowolony z tego co teraz powiem",
    "Ubert Hurbański: Bardzo mi przykro, ale",
    ]
    if wskaznik_progu>=3 and wskaznik_progu<=7:
        tekstr=random.randint(0,len(teksty_reklama_c)-1)
        print(teksty_reklama_c[tekstr],end='')
    else:
        tekstm=random.randint(0,len(teksty_reklama_m)-1)
        print(teksty_reklama_m[tekstm],end='')
        for i in range(0,3):
            time.sleep(0.5)
            print('.',end='')
            time.sleep(0.5)
        print("czas na przerwę.")
    time.sleep(3)
    os.system('cls')
    print(colored("Czy miałeś kiedyś ochotę na wyjazd w Bieszczady właśnie teraz, bez zastanowienia?",'red'))
    time.sleep(3)
    print(colored("Czy myślałeś kiedyś o tym, żeby spędzić miło czas wśród natury?",'green'))
    time.sleep(3)
    print(colored("Czy chciałbyś, żeby ktoś płacił Ci za bycie na wakacjach?",'yellow'))
    time.sleep(3)
    print(colored("Jeśli odpowiedź na którekolwiek z tych pytań to 'tak', trafiłeś w dobre miejsce!",'magenta'))
    time.sleep(3)
    print(colored("Bieszczadzkie ranczo 'HANYS' poszukuje pracowników na wypas owiec!",'magenta'))
    time.sleep(2)
    print(colored("Zadzwoń już teraz:",'red'))
    for i in range(0,3):
        print(random.randint(500,820),end='')
        if not i ==2:
            print("-",end='')
        time.sleep(0.7)
    time.sleep(4)
    os.system('cls')
    print("Ubert Hurbański: Wracamy po przerwie.")
    time.sleep(2)

def animacja():# Function for implementing the loading animation #source: https://www.geeksforgeeks.org/python-create-simple-animation-for-console-based-application/
    # String to be displayed when the application is loading
    load_str = "   milionerzy..."
    ls_len = len(load_str)


    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0

    while (counttime != 52):

        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)

        # for storing the resultant string
        res =''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res


        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

    # for windows OS
    if os.name =="nt":
        os.system("cls")

    # for linux / Mac OS
    else:
        os.system("clear")

#funkcja ktora wyswietla sie na poczatku programu, przed pytaniami
def powitanie():
    animacja()
    print(colored("\n\n         Witam Państwa!",'cyan'),"Mam na imię Ubert Hurbański i mam przyjemność powitać dzisiejszego zawodnika.")
    time.sleep(1)
    print("Zasady są następujące:",end='')
    time.sleep(1)
    print(" 12 pytań do miliona, 2 progi gwarantowane: 1000 zł i 40 000 zł oraz 3 koła ratunkowe:")
    time.sleep(1)
    print("                         telefon do przyjaciela,",end='')
    time.sleep(1)
    print(" pytanie do publiczności",end='')
    time.sleep(1)
    print(" i pół na pół.")
    time.sleep(1)
    print("                                   Gramy o milion, bądźcie państwo z nami!\n")
    time.sleep(1)
###################################################################################################################
def telefon_do_przyjaciela(lista_pytan, wylosowane_pytanie):
    global wskaznik_progu
    print("\nDzwonimy do przyjaciela.")
    for i in range(0,3):
        time.sleep(1.2)
        print("*",end='')
    time.sleep(1.2)
    print("\nLukasz Morawiecki, słucham?")
    time.sleep(2)
    print("Hej, Lukaszu, gram teraz w Millionerów.")
    time.sleep(2)
    print("Mam do Ciebie pytanie:", lista_pytan[wylosowane_pytanie][0])
    time.sleep(2)
    print("Czy możesz udzielić odpowiedzi?")
    tablica_dla_los = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"]   #LISTA Z KTÓREJ LOSUJEMY ODPOWIEDŻ KOLEGI
    for i in range(0,13-wskaznik_progu+random.randint(-1,3)): #zwiększamy w tym miejscu prawdopodobieństwo wylosowania prawidłowej odp
        tablica_dla_los.append(lista_pytan[wylosowane_pytanie][6])
    wylosowana_odpowiedz = random.choice(tablica_dla_los)#losuje nam odpowiedzi od abcd - im wyzszy numer pytania tym mniejsza szansa na poprawna odp
    for i in range(0,3):
        time.sleep(1.2)
        print("*",end='')
    time.sleep(1.2)
    print("\nUbert Hurbański: Panie Lukaszu, czy Pan juz moze podać odpowiedź?")
    time.sleep(1)
    print("Odpowiedź kolegi:", wylosowana_odpowiedz)

##########################################################################################################################
def kolo_pol_na_pol(lista_pytan, wylos_nr_pytania):     #kolo przyjmuje z argumenty listę pytań i numer danego pytania wylosowanego przez komputer
    print("Ubert Hurbański: Proszę o odrzucenie dwóch błędnych odpowiedzi.")
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
    nr_tekstu=random.randint(0,3)
    teksty=[
    "Ubert Hurbański: Proszę państwa, oto pytanie dla państwa.",
    "Ubert Hurbański: Proszę Państwa, prosimy o Państwa pomoc...",
    "Ubert Hurbański: Bardzo prosimy państwa o wsparcie.."
    ]
    print(teksty[nr_tekstutekst])
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
    global wskaznik_progu
    global lista_progow
    wyswietl_prog(lista_progow)
    print("Ubert Hurbański: Pytanie za",lista_progow[wskaznik_progu],"zł.")
    time.sleep(1.5)
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
        wybor_uzytkownika = input("Koła ratunkowe: 1 - telefon do przyjaciela; 2 - pol na pol; 3 - pytanie do publicznosci.\nDla rezygnacji wciśnij \"X\".\nCo wybierasz?\n")  #wpisywanie odpowiedzi #jak poprosic o wpisanie "A" czy "a"?
        if wybor_uzytkownika == lista_pytan[numer_pytania][6] or wybor_uzytkownika == lista_pytan[numer_pytania][7]:   #sprawdzanie czy wpisana odpowiedz prawdziwa; MA BYĆ NA 6 i 7 MIEJSCU PORZĄDKOWYM(DLA KOMPUTERA NA 5 i 6) W LIŚCIE!! #są dwa możliwe warianty wpisania "A" czy "a" - dlatego robimy (żeby nie przekształcać potem input) odrazu możliwość "A" czy "a".
            wskaznik_progu += 1
            if wskaznik_progu!=2 or wskaznik_progu!=7:
                pass
            if wskaznik_progu==2:
                wskaznik_progu_gw=1000
            if wskaznik_progu==7:
                wskaznik_progu_gw=40000
            print("Ubert Hurbański: Czy to poprawna odpowiedź?")
            for i in range(3,0,-1): #odlicza 321 po prawidlowej odpowiedzi, end="\r" znaczy ze nadpisuje aktualną linijkę, dlatego licznik wyswietla sie ladnie w jednym miejscu
                print(i,end="\r")
                time.sleep(0.4)
            if wskaznik_progu==5+random.randint(-2,2) or wskaznik_progu==11:
                reklama()
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
    print("\n MILIONERZY\n")
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
        if wskaznik_progu==0:
            print("\nUbert Hurbański: Zaczynajmy!\n")
            time.sleep(1)
        else:
            tekstyg=["Ubert Hurbański: To się dzieje naprawdę!",
            "Ubert Hurbański: Świetnie! Przechodzimy do kolejnego pytania.",
            "Ubert Hurbański: Bardzo dobrze! Przechodzimy do kolejnego pytania.",
            "Ubert Hurbański: Brawo! Przechodzimy do kolejnego pytania.",
            "Ubert Hurbański: To była poprawna odpowiedź! Przechodzimy do kolejnego pytania.",
            "Ubert Hurbański: Tak! Myślę, że kolejne pytanie Ci się spodoba.",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Brawo, to była poprawna odpowiedź!",
            "Ubert Hurbański: Tak, to była poprawna odpowiedź!",
            "Ubert Hurbański: Tak! Ale w tym pytaniu może przydać Ci się jedno z kół ratunkowych."]
            wybrany_tekst=random.randint(0,len(tekstyg)-1)
            print(tekstyg[wybrany_tekst])
            time.sleep(1.5)
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
        print("Ubert Hurbański: Brawo, to prawidłowa odpowiedź na ostatnie pytanie!")
        print("Ubert Hurbański: Właśnie wygrałeś MILION ZŁOTYCH!\n\nDziękujemy, że byliście Państwo z nami!")
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
            print("\nBardzo mi przykro, przegrałeś grę! Odchodzisz z kwotą:",wskaznik_progu_gw,"zł.\nDziękujemy, że byliście Państwo z nami!")
            break
        elif rezygnacja==1:
            os.system('cls')
            wyswietl_prog(lista_progow)
            print("Zrezygnowałeś z dalszej gry.\nOdchodzisz z kwotą:",lista_progow[wskaznik_progu],"zł.\nDziękujemy, że byliście Państwo z nami!")
            break
