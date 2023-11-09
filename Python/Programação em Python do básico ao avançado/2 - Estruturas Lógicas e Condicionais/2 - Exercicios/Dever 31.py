#31
n1 = float(input("Sua altura: "))
n2 = float(input("Qual seu peso: "))

if (n1 < 1.20) and (n2 <= 60):
    print("Classificação A")

elif (n1 < 1.20) and (n2 >= 60 and n2 <= 90):
    print("Classificação D")

elif (n1 < 1.20) and (n2 > 90):
    print("Classificação G")

if (n1 >= 1.20 and n1 <= 1.70) and (n2 <= 60):
    print("Classificação B")

elif (n1 >= 1.20 and n1 <= 1.70) and (n2 >= 60 and n2 <= 90):
    print("Classificação E")

elif (n1 >= 1.20 and n1 <= 1.70) and (n2 > 90):
    print("Classificação H")

if (n1 > 1.70) and (n2 <= 60):
    print("Classificação C")

elif (n1 > 1.70) and (n2 >= 60 and n2 <= 90):
    print("Classificação F")

elif (n1 > 1.70) and (n2 > 90):
    print("Classificação I")