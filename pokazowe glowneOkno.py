###################################################################################
#glowne ustawienia
from tkinter import *
from tkinter import ttk
glowneOkno=Tk()
glowneOkno.title("Milionerzy v2")
glowneOkno.geometry("720x600")
###################################################################################

###################################################################################

###################################################################################
#tekst w oknie
label = Label(glowneOkno, text='MILIONERZY')
label.place(relx=0.5, rely=0.08, anchor='s')
###################################################################################

###################################################################################
#odpowiedzi
przyciskA=Button(glowneOkno,text="Odpowiedź A",background='cyan')
przyciskA.place(relx=0.2, rely=0.7, anchor='s')

przyciskB=Button(glowneOkno,text="Odpowiedź B",background='cyan')
przyciskB.place(relx=0.6, rely=0.7, anchor='s')

przyciskC=Button(glowneOkno,text="Odpowiedź C",background='cyan')
przyciskC.place(relx=0.3, rely=0.8, anchor='s')

przyciskD=Button(glowneOkno,text="Odpowiedź D",background='cyan')
przyciskD.place(relx=0.6, rely=0.9, anchor='s')
###################################################################################

###################################################################################
#koła
przycisk_50_na_50=Button(glowneOkno, text ="50/50")
przycisk_50_na_50.place(relx=0.68, rely=0.15, anchor='s')

przycisk_telefon_do_przyjaciela=Button(glowneOkno, text="Tel. do prz.")
przycisk_telefon_do_przyjaciela.place(relx=0.78, rely=0.15, anchor='s')

przycisk_pytanie_do_publicznosci=Button(glowneOkno, text="Pyt. do pub.")
przycisk_pytanie_do_publicznosci.place(relx=0.95, rely=0.15, anchor='s')
###################################################################################

#rezygnacja

#wyjście z programu
przycisk_wyjsc_z_programu=Button(glowneOkno, text ="Wyjsc z programu", command=glowneOkno.quit)
przycisk_wyjsc_z_programu.place(relx=0.90, rely=0.99, anchor='s')


glowneOkno.mainloop()
