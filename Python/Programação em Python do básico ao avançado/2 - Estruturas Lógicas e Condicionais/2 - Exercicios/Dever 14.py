#14
n1 = float(input("Nota Trabalho: "))
n2 = float(input("Nota Avaliação: "))
n3 = float(input("Nota Exame: "))

if (n1 >=  0 and n1 <= 10) & (n2 >=  0 and n2 <= 10) & (n3 >=  0 and n3 <= 10):

    media = ((n1*2) + (n2*3) + (n3*5)) / (2+3+5)

    if media >= 5 and media <= 10:
        print(f"{media} : Passou")

    elif media >= 0 and media <= 2.9 :
        print(f"{media} : Reprovou")

    elif media >= 3 and media <= 4.9 :
        print(f"{media} : Ta de recuperação")

else:
    print("Valores invalidos")