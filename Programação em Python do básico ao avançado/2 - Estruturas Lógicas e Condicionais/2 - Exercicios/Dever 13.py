#13
#Formula
#https://cp21nb.wordpress.com/2018/08/23/python-media-ponderada/
n1 = float(input("Nota Prova 1: "))
n2 = float(input("Nota Prova 2: "))
n3 = float(input("Nota Prova 3: "))

#Se pra passar se tem q ter 60 pontos no final, então kada prova vale 100 pontos
if (n1 >=  0 and n1 <= 100) & (n2 >=  0 and n2 <= 100) & (n3 >=  0 and n3 <= 100):

    media = (n1*1) + (n2*1) + (n3*2) / (1+1+2)

    if media >= 60:
        print("Passou")
    else:
        print("Reprovou")
else:
    print("Valores invalidos")