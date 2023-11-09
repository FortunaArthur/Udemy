#60
l = []
lp = []

while True:

    try:
        n = float(input("Numero: "))

        l.append(n)

        if n % 2 == 0:
            lp.append(n)

        print(l)

        print("\n"
        "1 - soma \n"
        "2 - quantidade \n"
        "3 - média \n"
        "4 - o maior \n"
        "5 - o menor \n"
        "6 - média dos pares \n"
        "0 - pra sair \n")


        o = int(input("Qual tu escolhe: "))

        if o == 1:
            print(sum(l))

        elif o == 2:
            print(len(l))

        elif o == 3:
            mean = sum(l)/float(len(l))
            print(mean)

        elif o == 4:
            print(max(l))

        elif o == 5:
            print(min(l))

        elif o == 6:
            meanp = sum(lp)/float(len(lp))
            print(meanp)

        elif o == 0:
            print("Cabo")
            False
            break

        else:
            print("Opção errada")

    except ValueError:
        print("É NUMERO KRL")