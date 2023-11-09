#28
x = int(input("1° Valor: "))
y = int(input("2° Valor: "))
z = int(input("3° Valor: "))

print("Qual a metrica que vc quer aplicar a estes valores?" + "\n"
"1 : Geométrica" + "\n"
"2 : Ponderada" + "\n"
"3 : Harmônica" +  "\n"
"4 : Aritimética" + "\n")

e = int(input("Qual vc vai escolher: "))

if e == 1:
    f = ((x * y * z) ** 0.5) ** 3
    print(f"Valor: {f}")

elif e == 2:
    f = ((x + 2) * (y + (3 * z))) / 6
    print(f"Valor: {f}")

elif e == 3:
    f = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f"Valor: {f}")

elif e == 4:
    f = (x + y + z) / 3
    print(f"Valor: {f}")

else:
    print("Opção invalida")