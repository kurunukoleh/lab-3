x = int(input("Illość użytkowników"))
n = int(input("illość potraw"))
l =[]

while len(l) != n:
    l.append(int(input("cena potrawy")))

print(sum(l)*x)