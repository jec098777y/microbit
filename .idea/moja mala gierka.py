print("wpisz liczbe do pomnozenia")
a = int(input())
print("teraz wpisz przez ile to pomnoze")
b = int(input())
odp = a * b
print("to wyjdzie", " ", odp)
print("czy chcerz podzielic ta cyfre?")
if input() == "tak":
    print("wpisz liczbe do podzielenia")
    c = int(input())
    d = odp
    d = c / d
    print("to wyjdzie", d)

elif input() == "nie":
    print("no dobrze sprubuj ponownie pomnozyc")



