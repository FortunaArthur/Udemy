#45
while True:
    o = int(input("1 - Converter km/h pra m/s\n"
    "2 - Converter m/s pra km/h\n"
    "3 - finalizar o programa \n"
    "Qual tu escolhe: "))

    if o == 1:
        n = float(input("Quantos Km ?: "))
        m = n / 3.6
        print(f"De {n} km/h foi pra {m} m/s\n")

    elif o == 2:
        n = float(input("Quantos m ?: "))
        m = n * 3.6
        print(f"De {n} m/s foi pra {m} km/h\n")

    elif o == 3:
        print("Cabou")
        False
        break