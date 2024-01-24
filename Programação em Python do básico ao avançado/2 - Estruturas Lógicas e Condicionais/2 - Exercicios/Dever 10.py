#10
h = float(input("Digite sua altura: "))
s = input("Digite seu sexo (M/F): ").upper()

if s == "M":
    f = (72.7 * h) - 58
    print(f"Seu peso ideal é {round(f)} kg")
else:
    f = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {round(f)} kg")