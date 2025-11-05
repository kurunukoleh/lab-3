licznik = 0
a = []


while licznik <= 29:
    licznik += 1
    for i in range(2 , licznik):
        if licznik % i == 0:
            a.append(False)
        else:
            a.append(True)
    if False not in a :
        print(licznik)
    a=[]