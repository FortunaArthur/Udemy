#32
v = int(input("vezes: "))
count = 0

while count < v:

    d1 = int(input("Dado 1: "))
    d2 = int(input("Dado 2: "))

    count += 1
    if count == v+1:
        break

    else:
        if d1 == d2:
            print("Valores iguais")

        elif d1 > d2:
            print(f"{d1} > {d2}")

        else:
            print(f"{d2} > {d1}")
