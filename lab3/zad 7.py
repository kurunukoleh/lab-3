n = int(input("Illość studentów"))
l = []

while True:
    i = int(input("ocena"))
    if 100 >= i >= 0:
        l.append(i)
    else:
        print("to nie jest ocena")

    if len(l) == n:
        break

print(sum(l)/n)