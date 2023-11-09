#29
print("Prova de Matematica" + "\n"
"Quanto é" + "\n"
"1 : 50 + 49" + "\n"
"2 : 10 + 39" + "\n"
"3 : 27 + 9" + "\n"
"4 : 31 + 49" + "\n"
"5 : 22 + 18" + "\n")

n1 = int(input("Questão 1: "))
n2 = int(input("Questão 2: "))
n3 = int(input("Questão 3: "))
n4 = int(input("Questão 4: "))
n5 = int(input("Questão 5: "))

acertos = 0

if n1 == (50 + 49):
    print(f"Acertou, a resposta é {50 + 49}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {50 + 49}")

if n2 == (10 + 39):
    print(f"Acertou, a resposta é {10 + 39}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {10 + 39}")

if n3 == (27 + 9):
    print(f"Acertou, a resposta é {27 + 9}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {27 + 9}")

if n4 == (31 + 49):
    print(f"Acertou, a resposta é {31 + 49}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {31 + 49}")

if n4 == (22 + 18):
    print(f"Acertou, a resposta é {22 + 18}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {22 + 18}")

print(f"Vc acertou {acertos} questões")