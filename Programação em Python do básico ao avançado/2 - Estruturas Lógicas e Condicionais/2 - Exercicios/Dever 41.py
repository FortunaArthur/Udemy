#41
a = float(input("Qual sua altura: "))
p = float(input("Qual seu peso: "))

f = p / (a*a)

if f < 18.5:
    print("Abaixo do peso")

elif f >= 18.6 and f <= 24.9:
    print("Saudével")

elif f >= 25 and f <= 29.9:
    print("Tá gordo")

elif f >= 30 and f <= 34.9:
    print("Gordo p krl")

elif f >= 35 and f <= 39.9:
    print("Gordo extratosferico")

elif f >= 40:
    print("Eu conheço 20 gordos e vc é 19 deles")

else:
    print("Numero invalido")