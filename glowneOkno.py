def koniec_gry(): #funkcja ktora czysci caly ekran (niszczy wszystkie przyciski i napisy)
    tytul.destroy()
    dialogi.destroy()
    progi.destroy()
    przyciskA.destroy()
    przyciskB.destroy()
    przyciskC.destroy()
    przyciskD.destroy()
    przycisk_50_na_50.destroy()
    przycisk_telefon_do_przyjaciela.destroy()
    przycisk_pytanie_do_publicznosci.destroy()

def zrezygnuj(): #funkcja ktora zmienia zmienna rezygnacja na 1
    global rezygnacja
    rezygnacja=1
    print("rezygnacja:", rezygnacja) #testowo niech wyswietla w konsoli, zeby bylo widac czy cos sie zmienia


def wywolaj_tel_do_prz():
    telefon_do_przyjaciela(lista_pytan,aktualne_pytanie)
def wywolaj_50_na_50():
    kolo_pol_na_pol(lista_pytan,aktualne_pytanie)
def wywolaj_pyt_do_pub():
    publicznosc(lista_pytan,aktualne_pytanie)

###################################################################################
#glowne ustawienia
import random
import time
import os
import sys
from colorama import init, Style
from termcolor import colored
from funkcje import *
init()
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
###################################################################################
lista_progow = ["500","1 000","2 000","5 000","10 000","20 000","40 000","75 000","125 000","250 000","500 000","1 000 000","0"]
wskaznik_progu = 0
wskaznik_progu_gw = 0
###################################################################################
przegrana = 0
rezygnacja = 0
telefon_został_wykorzystany = 0
pytdopub_został_wykorzystany = 0
polnapol_został_wykorzystany = 0
###################################################################################
#ustawienia GUI
from tkinter import *
from tkinter import ttk


glowneOkno=Tk()
glowneOkno.title("Milionerzy v2") #górna belka głównego okna
glowneOkno.geometry("850x600") #rozmiar głownego okna

###################################################################################
#napis MILIONEZY w oknie
tytul = Label(glowneOkno, text='MILIONERZY', font=('times', 24, 'bold')) #gdzie wstawic tekst, jaki oraz jego czcionka i wielkosc
tytul.place(relx=0.5, rely=0.1, anchor='s') #zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac
###################################################################################
#okno z dialogiami
dialogi = Text(glowneOkno)
dialogi.insert(END, "hey")
dialogi.place(relx=0.1, rely=0.5, anchor='s',width=150,height=250)

###################################################################################
#odpowiedzi
przyciskA=Button(glowneOkno,text="Odpowiedź A",background='cyan',borderwidth=8) #background to kolor przycisku, borderwidth to taka mini ramka naokolo przycisku
przyciskA.place(relx=0.4, rely=0.7, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przyciskB=Button(glowneOkno,text="Odpowiedź B",background='cyan',borderwidth=8)#background to kolor przycisku, borderwidth to taka mini ramka naokolo przycisku
przyciskB.place(relx=0.6, rely=0.7, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przyciskC=Button(glowneOkno,text="Odpowiedź C",background='cyan',borderwidth=8)#background to kolor przycisku, borderwidth to taka mini ramka naokolo
przyciskC.place(relx=0.4, rely=0.8, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przyciskD=Button(glowneOkno,text="Odpowiedź D",background='cyan',borderwidth=8)#background to kolor przycisku, borderwidth to taka mini ramka naokolo przycisku
przyciskD.place(relx=0.6, rely=0.8, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac
###################################################################################

###################################################################################
#koła
przycisk_50_na_50=Button(glowneOkno, text ="50/50",background='cyan',borderwidth=8,command=wywolaj_50_na_50)#background to kolor przycisku, borderwidth to taka mini ramka naokolo przycisku
przycisk_50_na_50.place(relx=0.85, rely=0.15, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przycisk_telefon_do_przyjaciela=Button(glowneOkno, text="Tel. do prz.",background='cyan',borderwidth=8,command=wywolaj_tel_do_prz)#background to kolor przycisku, borderwidth to taka mini ramka naokolo przycisku
przycisk_telefon_do_przyjaciela.place(relx=0.75, rely=0.15, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przycisk_pytanie_do_publicznosci=Button(glowneOkno, text="Pyt. do pub.",background='cyan',borderwidth=8, command=wywolaj_pyt_do_pub)#background to kolor przycisku, borderwidth to taka mini ramka naokolo
przycisk_pytanie_do_publicznosci.place(relx=0.95, rely=0.15, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac
###################################################################################

#rezygnacja

#wyjście z programu
przycisk_wyjsc_z_programu=Button(glowneOkno, text ="Wyjsc z programu", command=glowneOkno.quit)#jesli nacisniemy przycisk, to zamknij cale okno
przycisk_wyjsc_z_programu.place(relx=0.90, rely=0.99, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac

przycisk_rezygnacja=Button(glowneOkno, text ="Zrezygnuj", command=lambda:[koniec_gry(),zrezygnuj()]) #ustawienia przycisku (lambda wyglada strasznie ale po prostu wywoluje dwie funkcje naraz, i tyle)
przycisk_rezygnacja.place(relx=0.9, rely=0.93, anchor='s')#zwykłe .place, ale zamiast podawać x oraz y pixelowo, to podajemy je procentowo, anchor nie zmienia za wiele ale musi zostac
progi = Label(glowneOkno, text='1 000 000\n500 000\n250 000\n125 000\n75 000\n40 000\n20 000\n10 000\n5 000\n2 000\n1 000\n500') #gdzie wstawic tekst, jaki oraz jego czcionka i wielkosc
progi.place(relx=0.85, rely=0.60, anchor='s')


rozmiar_listy = len(lista_pytan)
kolejnosc_pytan = generacja_kolejnosci_pytan(rozmiar_listy)

obecny = 0

glowneOkno.mainloop() #odpal cale okno
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
glowneOkno.mainloop()
