#6
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
    print(f"Diferença {n1-n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
    print(f"Diferença {n2-n1}")
else:
    print("Numeros iguais")