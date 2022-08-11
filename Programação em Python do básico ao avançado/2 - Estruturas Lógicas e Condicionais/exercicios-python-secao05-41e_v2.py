#1
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Numeros iguais")

#2
n = float(input("Numero: "))
if n > 0:
    print(f"Raiz quadrada {n**0.5}")
else:
    print("Numero invalido")

#3
n = float(input("Numero: "))
if n > 0:
    print(f"Raiz quadrada {n**0.5}")
else:
    print(f"Seu quadrado {n*n}")

#4
n = float(input("Numero: "))
if n > 0:
    print(f"Seu quadrado {n*n}")
    print(f"Raiz quadrada {n**0.5}")
else:
    print("Numero negativo")

#5
n = int(input("Numero: "))

if (n % 2) == 0:
    print('Número é par')
elif (n % 2) == 1:
    print('Número é impar')
else:
    print("É 0")

#6
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
    print(f"Diferença {n1-n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
    print(f"Diferença {n2-n1}")
else:
    print("Numeros iguais")

#7
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Numeros iguais")

#8
n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))

if (n1 >= 0 and n1 <= 10) & (n2 >= 0 and n2 <= 10):
    media = (n1+n2)/2
    print(f"A media das notas é {media}")
else:
    print("Valores invalidos")

#9
n1 = float(input("Digite seu salario: "))
n2 = float(input("Digite a prestação do emprestimo: "))

p = (n2 * 100) / n1

if p > 20:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")

#10
h = float(input("Digite sua altura: "))
s = input("Digite seu sexo (M/F): ").upper()

if s == "M":
    f = (72.7 * h) - 58
    print(f"Seu peso ideal é {round(f)} kg")
else:
    f = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {round(f)} kg")

#11
#Encontrei nesse site em C e adaptei pra python
#https://www.portugal-a-programar.pt/forums/topic/23208-programa-que-leia-um-n%C3%BAmero-inteiro-e-calcule-a-soma-dos-seus-d%C3%ADgitos/
#https://www.youtube.com/watch?v=5i5hmY6j7dM
''''''''''''''''''''''
numero = int(input("numero :  "))

somatorio=0

while (numero>0):

    resto = numero % 10
    numero = (numero-resto) / 10
    somatorio = somatorio + resto

print(f"O somatório é {somatorio}")
'''''''''''''''''''''''
#Também encontrei de outra forma mais simples usando MAP() e SUM()
#https://acervolima.com/programa-python-para-somar-os-digitos-de-um-determinado-numero/#:~:text=O%20m%C3%A9todo%20int()%20%C3%A9,dos%20d%C3%ADgitos%20em%20cada%20itera%C3%A7%C3%A3o.&text=M%C3%A9todo%202%3A%20Usando%20m%C3%A9todos%20sum,somar%20os%20n%C3%BAmeros%20na%20lista.
#tem q colocar o N como string pro map converter, acho que é isso, eu não entendi mt bem
''''''''''''''''''''''
n = str(input("Numero:  "))

list_of_number =map(int, n) 

print(  (sum(list_of_number)) )
'''''''''''''''''''''
#isso aki ajudou
#https://www.geeksforgeeks.org/python-map-function/
#http://devfuria.com.br/python/built-in-list/
#Peguei a manha

n = int(input("Numero:  "))

if n > 0:
    #convertelo pra string e dps pra lista
    m = list(str(n))
    #pro map() fazer o mapeamento e converter em inteiro
    lista_numero =map(int, m) 
    #dps sola-lo
    print(  (sum(lista_numero)) )

else:
    print("Numero invalido")

#12
#http://www.w3big.com/pt/python/func-number-log.html
from ast import Not
import math
from re import A, X
from tkinter.tix import InputOnly
n = int(input("Numero:  "))

if n > 0:
    print(f"Logaritimo de {n} é {math.log(n)}")
else:
    print("Numero invalido")

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

#15
n = int(input("Numerode 1 a 7: "))

d = {1: "Domingo", 2: "Segunda",3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sabado"}

if n >= 1 and n <= 7:
    for i in d:
        if n == i:
            print(d[i])
else:
    print("Valor invalido")

#16
n = int(input("Numerode 1 a 12: "))

m = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

if n >= 1 and n <= 12:
    for i in m:
        if n == i:
            print(m[i])
else:
    print("Valor invalido")

#17
BM = float(input("Base Maior: "))
bm = float(input("Base Menor: "))
h = float(input("Altura: "))

a = ((BM + bm) * h)/2

if (BM > 0) & (bm > 0) & (h > 0): 
    print(f"Área do Trapézio: {a}")
else:
    print("Valores errados")

#18
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

print("MENU" + "\n" 
"1 : Somar" + "\n"
"2 : Subtrair" + "\n"
"3 : Dividir" + "\n"
"4 : Multiplicar" + "\n")

escolha = int(input("Qual opção vc escolhe: "))

if escolha == 1:
    print(f"{n1} + {n2} = {n1+n2}")
    
elif escolha == 2:
    print(f"{n1} - {n2} = {n1-n2}")

elif escolha == 3:
    print(f"{n1} / {n2} = {n1/n2}")
    
elif escolha == 4:
    print(f"{n1} * {n2} = {n1*n2}")

else:
    print("Valor errado")

#19
#Inspiração
#https://wagnergaspar.com/exercicio-3-leia-um-numero-e-informe-se-ele-e-divisivel-por-2-por-3-ou-por-5/
n = int(input("asdfa: "))

if (n % 3 == 0) or (n % 5 == 0):
    print("Divisivel")
    
else:
    print("valor errado")

#20
#peguei daki, fikei cansado p krl, exercicio de corno essa questão
#https://www.pythonprogressivo.net/2018/02/Curso-Triangulo-Equilatero-Isosceles-Escaleno.html
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

# Testando se é triângulo
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
    
#Triângulo Equilátero: três lados iguais;
elif (a == b) and (a == c) :
    print('Equilatero')

#Triângulo Isósceles: quaisquer dois lados iguais;
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')

#Triângulo Escaleno: três lados diferentes;
else:
    print('Escaleno')

#21
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

print("MENU" + "\n" 
"1 : Somar" + "\n"
"2 : Subtrair Maior pelo Menor" + "\n"
"3 : Produto entre os 2 (Multiplicação)" + "\n"
"4 : Divisão entre os 2 (Não pode ser numero 0)" + "\n")

escolha = int(input("Qual opção vc escolhe: "))

if escolha == 1:
    print(f"{n1} + {n2} = {n1+n2}")
    
elif escolha == 2:
   if n1 > n2:
    print(f"{n1} - {n2} = {n1-n2}")
   else:
    print(f"{n2} - {n1} = {n2-n1}")

elif escolha == 3:
    print(f"{n1} * {n2} = {n1*n2}")
    
elif escolha == 4:
    if n1 and n2 > 0:
        print(f"{n1} / {n2} = {n1/n2}")
        print(f"{n2} / {n1} = {n2/n1}")
    else:
        print("Valor 0 não divide")

else:
    print("Valor errado")

#22
n1 = int(input("Qual sua idede: "))
n2 = int(input("Quantos anos vc prestou serviço: "))

if n1 >= 65:
    print("Pode Aposentar")

elif n2 >= 30:
    print("Pode Aposentar")

elif (n1 >= 65) and (n2 >= 30):
    print("Pode Aposentar")

else:
    print("Não pode Aposentar")

#23
n = int(input("Qual o ano: "))

if n % 400 == 0:
    print("Ano Bissexto")

elif (n % 4 == 0) and not (n % 100 == 0):
    print("Ano Bissexto")

else:
    print("Ano Não Bissexto")

#24
n = float(input("Qul o valor do produto: "))
print("Imposto sobre o produto por estado" + "\n"
"MG : 07%" + "\n"
"SP : 12%" + "\n"
"RJ : 15%" + "\n"
"MS : 08%" + "\n")
i = input("Pra qual estado o produto será enviado: ").upper()

if i == "MG":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 7) / 100)}")

elif i == "SP":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 12) / 100)}")

elif i == "RJ":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 15) / 100)}")

elif i == "MS":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 8) / 100)}")

else:
    print("Erro de estado")

#25
D = (b**2) - (4 * (a * c))

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

if a != 0:
    print("Não é equação de 2° grau")

else:
    if D < 0:
        print("Não existe raiz")
    
    elif D == 0:
        print(f"{(-b + (D ** 0.5)) / (2 * a)}")
        print("Raiz Unica")
    
    elif D >= 0:
        print(f"1° raiz : {(-b + (D ** 0.5)) / (2 * a)}")
        print(f"2° raiz : {(-b - (D ** 0.5)) / (2 * a)}")

#26
n = float(input("Km: "))
l = float(input("Litros: "))

f = n / l

if f < 8:
    print("Vende esse carro")

elif f >= 8 and f <=14:
    print("Economico")

elif f > 14:
    print("Economico pra krl")

#27
n = int(input("Qual tua idade: "))

if n >= 5 and n <= 7:
    print("Infantil A")

elif n >= 8 and n <= 10:
    print("Infantil B")

elif n >= 11 and n <= 13:
    print("Juvenil A")

elif n >= 14 and n <= 17:
    print("Juvenil B")

else:
    print("Sênior")

#28
x = int(input("1° Valor: "))
y = int(input("2° Valor: "))
z = int(input("3° Valor: "))

print("Qual a metrica que vc quer aplicar a estes valores?" + "\n"
"1 : Geométrica" + "\n"
"2 : Ponderada" + "\n"
"3 : Harmônica" +  "\n"
"4 : Aritimética" + "\n")

e = int(input("Qual vc vai escolher: "))

if e == 1:
    f = ((x * y * z) ** 0.5) ** 3
    print(f"Valor: {f}")

elif e == 2:
    f = ((x + 2) * (y + (3 * z))) / 6
    print(f"Valor: {f}")

elif e == 3:
    f = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f"Valor: {f}")

elif e == 4:
    f = (x + y + z) / 3
    print(f"Valor: {f}")

else:
    print("Opção invalida")

#29
print("Prova de Matematica" + "\n"
"Quanto é" + "\n"
"1 : 50 + 49" + "\n"
"2 : 10 + 39" + "\n"
"3 : 27 + 9" + "\n"
"4 : 31 + 49" + "\n"
"5 : 22 + 18" + "\n")

n1 = int(input("Questão 1: "))
n2 = int(input("Questão 2: "))
n3 = int(input("Questão 3: "))
n4 = int(input("Questão 4: "))
n5 = int(input("Questão 5: "))

acertos = 0

if n1 == (50 + 49):
    print(f"Acertou, a resposta é {50 + 49}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {50 + 49}")

if n2 == (10 + 39):
    print(f"Acertou, a resposta é {10 + 39}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {10 + 39}")

if n3 == (27 + 9):
    print(f"Acertou, a resposta é {27 + 9}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {27 + 9}")

if n4 == (31 + 49):
    print(f"Acertou, a resposta é {31 + 49}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {31 + 49}")

if n4 == (22 + 18):
    print(f"Acertou, a resposta é {22 + 18}")
    acertos = acertos + 1
else:
    print(f"Errou, a resposta é {22 + 18}")

print(f"Vc acertou {acertos} questões")

#30
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

l = [n1,n2,n3]

print(f"Ordem crescente: {sorted(l)}")

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

#32
print("Cardapio | Codigo | Preço" + "\n"
"Dogão | 100 | 1.20"  + "\n"
"Bauru simples | 101 | 1.30"  + "\n"
"Bauru com ovo | 102 | 1.50"  + "\n"
"Hamburgão | 103 | 1.20"  + "\n"
"Hamburgão com queijo | 104 | 1.70"  + "\n"
"Sukinho | 105 | 2.20"  + "\n"
"Refri | 106 | 1.00"  + "\n")

cod = int(input("Qual o codigo: "))

if cod == 100:
    print("Vc vai pagar 1.20 pelo hotdog")
else:
    if cod == 101:
        print("Vc vai pagar 1.30 pelo Bauru simples")
    else:
        if cod == 102:
            print("Vc vai pagar 1.50 pelo Bauru com ovo")
        else:
            if cod == 103:
                print("Vc vai pagar 1.20 pelo Hamburgão")
            else:
                if cod == 104:
                    print("Vc vai pagar 1.70 pelo Hamburgão com queijo")
                else:
                    if cod == 105:
                        print("Vc vai pagar 2.20 pelo Sukinho")
                    else:
                        if cod == 106:
                            print("Vc vai pagar 1.00 pelo Refri")

#33
n = float(input("Preço do produto: "))

if n <= 50:
    f = n + ((n * 5) / 100)
    if f <= 80:
        print("Barato")

if n > 50 and n1 <= 100:
    f = n + ((n * 10) / 100)
    if f > 80 and f <= 120:
        print("Normal")

if n > 100:
    f = n + ((n * 15) / 100)
    if f > 120 and f <= 200:
        print("Caro")
    elif n > 200:
        print("Caro p krl")

else:
    print("Erro")

#34
n = float(input("Qual sua nota: "))
f = int(input("Quantas faltas vc tem: "))

if (n >= 9) and (n <= 10):
    if f <= 20:
        print("Conceito: A")
    else:
        print("Conceito: B")

if (n >= 7.5) and (n <= 8.9):
    if f <= 20:
        print("Conceito: B")
    else:
        print("Conceito: C")

if (n >= 5) and (n <= 7.4):
    if f <= 20:
        print("Conceito: C")
    else:
        print("Conceito: D")

if (n >= 4) and (n <= 4.9):
    if f <= 20:
        print("Conceito: D")
    else:
        print("Conceito: E")

if (n >= 0) and (n <= 3.9):
    if f <= 20:
        print("Conceito: E")
    else:
        print("Conceito: E")

#35
#Fikei sem saco pra essa e peguei aki
#https://www.pythonprogressivo.net/2018/02/Determinar-Data-Valida-Invalida.html

dia = int( input('Dia: ') )
mes = int( input('Mês: ') )
ano = int( input('Ano: ') )

valida = False

# Meses com 31 dias
if( mes==1 or mes==3 or mes==5 or mes==7 or \
    mes==8 or mes==10 or mes==12):
    if(dia<=31):
        valida = True
# Meses com 30 dias
elif( mes==4 or mes==6 or mes==9 or mes==11):
    if(dia<=30):
        valida = True
elif mes==2:
    # Testa se é bissexto
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        if(dia<=29):
            valida = True
    elif(dia<=28):
            valida = True

if(valida):
    print('Data válida')
else:
    print('Inválida')

#36