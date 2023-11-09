#26
n = float(input("Km: "))
l = float(input("Litros: "))

f = n / l

if f < 8:
    print("Vende esse carro")

elif f >= 8 and f <=14:
    print("Economico")

elif f > 14:
    print("Economico pra krl")