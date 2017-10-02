#Guess the Number

import random

print("Witaj! Zgadnij liczbę z przediału <1;100>. Masz 6 prób \n")
wylosowana = random.randint(1, 100)
zgadywana = 0
proba = 0

while proba < 6 and zgadywana != wylosowana:
    zgadywana = int(input("Zgaduj liczbę: "))
    if zgadywana > wylosowana:
        print("Podałeś za dużą liczbę")
    elif zgadywana < wylosowana:
        print("Podałeś za małą liczbę")
    proba += 1

if zgadywana != wylosowana:
    print("Niestety, wykorzystałeś już 6 prób i nie odgadłeś liczby")
    print("Wylosowana liczba to: ", wylosowana)
else:
    print("Gratulacje! Udało Ci się, ilość prób: ", proba)


    
