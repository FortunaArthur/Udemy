#23
n = int(input("Qual o ano: "))

if n % 400 == 0:
    print("Ano Bissexto")

elif (n % 4 == 0) and not (n % 100 == 0):
    print("Ano Bissexto")

else:
    print("Ano Não Bissexto")