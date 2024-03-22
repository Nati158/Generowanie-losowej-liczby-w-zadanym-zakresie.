import random

def losowa_liczba(minimum, maksimum):
    return random.randint(minimum, maksimum)

minimum = int(input("Podaj dolny zakres: "))
maksimum = int(input("Podaj górny zakres: "))

wylosowana = losowa_liczba(minimum, maksimum)
print("Wylosowana liczba:", wylosowana)
