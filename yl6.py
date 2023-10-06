#yl6.py
#Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
#(loogikatehted - logic operators)

a = int (input("sisesta arv a: "))
b = int (input("sisesta arv b: "))
c = int (input("sisesta arv c: "))

if a > b and a > c:
    print("maksimum on", a)

elif b > c:
    print("maksimum on", b)

else:
    print("maksimum on", c)
