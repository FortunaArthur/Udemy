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
from re import A
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
