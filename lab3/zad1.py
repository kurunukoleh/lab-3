paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    paliwo -= paliwo_zużyte_na_s
    print(paliwo)

print("Koniec lotu")