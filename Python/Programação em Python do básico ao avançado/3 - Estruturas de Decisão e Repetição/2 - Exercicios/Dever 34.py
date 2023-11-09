#34
#Peguei essa porra dessa merda aki
# https://pt.stackoverflow.com/questions/439722/obter-o-menor-n%C3%BAmero-positivo-que-%C3%A9-divis%C3%ADvel-por-todos-os-n%C3%BAmeros-de-1-a-20
# VSF DEVER DE CORNO
i = 1
numero = int(input("Numero: "))
while i != 0:
    if numero % 1 == 0 and numero % 2 == 0 and numero % 3 == 0 and numero % 4 == 0 and numero % 5 == 0 and numero % 6 ==\
            0 and numero % 7 == 0 and numero % 8 == 0 and numero % 9 == 0 and numero % 10 == 0 and numero % 11 == 0\
              and numero % 12 == 0 and numero % 13 == 0 and numero % 14 == 0 and numero % 15 == 0 and numero % 16 == 0 \
              and numero % 17 == 0 and numero % 18 == 0 and numero % 19 == 0 and numero % 20 == 0:
        print(numero)
        i = 0
    else:
        numero += 1