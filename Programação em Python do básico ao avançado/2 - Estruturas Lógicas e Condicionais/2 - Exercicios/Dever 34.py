#34
n = float(input("Qual sua nota: "))
f = int(input("Quantas faltas vc tem: "))

if (n >= 9) and (n <= 10):
    if f <= 20:
        print("Conceito: A")
    else:
        print("Conceito: B")

if (n >= 7.5) and (n <= 8.9):
    if f <= 20:
        print("Conceito: B")
    else:
        print("Conceito: C")

if (n >= 5) and (n <= 7.4):
    if f <= 20:
        print("Conceito: C")
    else:
        print("Conceito: D")

if (n >= 4) and (n <= 4.9):
    if f <= 20:
        print("Conceito: D")
    else:
        print("Conceito: E")

if (n >= 0) and (n <= 3.9):
    if f <= 20:
        print("Conceito: E")
    else:
        print("Conceito: E")