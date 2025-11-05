

name = input("Wpisz imię")
print("Witaj" , str(name))

age = input("Twój wiek to:")
print("Twój wiek to:", str(age))


surname = input("nazwisko")
print(name[0].upper() + surname[0].upper())

chain = input("łańcuch")
for i in range(5):
    print(chain)

text1 = input("Wpisz coś")
text2 = input("Wpisz coś")
text = text1 + text2
print(text)
print(text[:(len(text)//2)])

