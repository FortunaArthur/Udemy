#8
n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))

if (n1 >= 0 and n1 <= 10) & (n2 >= 0 and n2 <= 10):
    media = (n1+n2)/2
    print(f"A media das notas é {media}")
else:
    print("Valores invalidos")