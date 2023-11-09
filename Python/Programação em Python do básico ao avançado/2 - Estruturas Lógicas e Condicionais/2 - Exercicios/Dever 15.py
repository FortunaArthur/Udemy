#15
n = int(input("Numerode 1 a 7: "))

d = {1: "Domingo", 2: "Segunda",3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sabado"}

if n >= 1 and n <= 7:
    for i in d:
        if n == i:
            print(d[i])
else:
    print("Valor invalido")