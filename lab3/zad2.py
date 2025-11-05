licznik = 0
a = False


while licznik <= 29:
    licznik+=1
    for i in range(2 , licznik):
        if licznik % i == 0:
            a = True
        else:
            a = False
    if a :
        print(licznik)