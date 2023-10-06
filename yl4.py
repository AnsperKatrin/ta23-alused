#yl4.py
#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
#(muutuja - variable, tingimus - condition, if-lause - if statement)

a = input("Sisesta a: ")
b = input("Sisesta b: ")
if int (b) > int (a):
    print("miinimum on", a)
else:
    print("miinimum on", b)


