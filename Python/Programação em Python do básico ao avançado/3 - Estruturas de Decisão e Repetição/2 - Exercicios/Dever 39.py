#39
t = 0
while t == 0:
    try:
        b = int(input("Base: "))
        h = int(input("Altura: "))

        if b and h > 0:
            a =( b*h)/2
            print(f"Area é igual a {a}")
            t+=1
            break
        else:
            print("Não pode ter valor menos q 0")

    except ValueError:
        print("É só inteiro")