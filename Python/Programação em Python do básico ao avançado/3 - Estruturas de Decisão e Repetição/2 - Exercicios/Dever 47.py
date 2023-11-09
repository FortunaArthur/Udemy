#47
n1 = int(input("N1: "))
n2 = int(input("N2: "))

while True:
    o = int(input(
    "\n1 - Adição\n"
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão\n"
    "5 - Saida\n"
    "Qual tu escolhe: ""\n"))

    if o == 1:
        print(n1+n2)

    elif o == 2:
        print(n1-n2)

    elif o == 3:
        print(n1*n2)

    elif o == 4:
        print(n1/n2)

    elif o == 5:
        print("Cabou")
        False
        break