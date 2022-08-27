#1
# for i in rane (inicio, fim, incremento(Que vai  pulando))
for i in range(3, 16, 3):
# Ele vai inicializar com 3 e vai terminar com 16 e vai fazer o incremento de 3 em 3 (soma de 3 em 3)
    print(i)

#2
for i in range (1,101):
    print(i)

n = 1
while n < 100:
  n = n + 1
  print(n)

n = 0
while True:
  n = n + 1
  print(n)
  if n == 100:
    break

#3
n = 11
while n > 0:
  n = n - 1
  print(n)

#4
for i in range (0, 101000, 1000):
    print(i)

#5
s = 0
for i in range (1,11):
  a = int(input("Numero: "))
  s = s + a
  print(s)

#6
s = 0 #  SOMA
q = 0 # N° DE VEZES DIGITADOS
for i in range (1,11):
  a = int(input("Numero: "))
  s = s + a # SOMA DOS INPUTS
  q = q + 1 # SOMA DAS VEZES
# : . 2f é pra colocar só 2 casas decimais
print(f"Média: {s/q:.2f}")

#7
#FOR
s = 0 #  SOMA
q = 0 # N° DE VEZES DIGITADOS
for i in range (1,11):
  a = int(input("Numero: "))
  if a > 0:
    s = s + a # SOMA DOS INPUTS
    q = q + 1 # SOMA DAS VEZES
  
  else:
    print("Não conta")

# : . 2f é pra colocar só 2 casas decimais
print("Soma: ", s)
print(f"Média: {s/q:.2f}")

#WHILE
soma = 0
quantidade = 0
while True:
  
  n = int(input("Digite um número inteiro: "))
  
  if n > 0:
    soma = soma + n
  else:
    print("Não conta")
  
  quantidade = quantidade + 1

  if quantidade == 10:
    break
  
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")

#8
#O dever de corno
n = 0
l = []
while n < 10:
  n = n + 1
  i = int(input("Numeros: "))
  l.append(i)

print(f"Maior: {max(l)}, Menor: {min(l)}")

#9
n = 1 #vezes
l = []

while n <= 10:
  a = int(input("Numero: "))
  n = n + 1
  if a % 2 != 0:
    l.append(a)

print(f"Lista de Impares:  {l}")

#OU

n = int(input("Numero: "))
for i in range(1, n+1):
  if i % 2 != 0:
    print(i, end=". ")

#10
n = int(input("Numero: "))
for i in range(1, n+1):
  if i % 2 == 0:
    print(i, end=". ")

#11
n = int(input("Numero; "))
for i in range (1,n+1):
    print(i)
  
#12
n = int(input("Numero: "))
while n > 0:
  n = n - 1
  print(n)

#13
n = int(input("Numero: "))
for i in range(1, n+1):
  if i % 2 == 0:
    print(i, end=". ")

#14
n = int(input("Numero: "))
while n > 0:
  n = n - 1
  if n % 2 == 0:
    print(n)

#15
n = int(input("Numero: "))
for i in range(1, n+1):
  if i % 2 != 0:
    print(i, end=". ")

#16
n = int(input("Numero: "))
while n > 0:
  n = n - 1
  if n % 2 != 0:
    print(n)

#17
n = int(input("Numero: "))
N = 0
for i in range(1, n+1):
  N += i 
print(f"SOMA: {N}")

#18
v = int(input("Vezes: "))
l = []

for i in range(0, v):
  n = int(input("Numeros: "))
  l.append(n)
  m = max(l)
  c = l.count(m)
  
print(f"O numero max foi {m} e ele se repetiu {c} vezes")

#19
while True:
    a = (int(input('insira um numero entre 100 e 999: ')))
    
    if a > 100 and a < 999:
       break
   
    else:
        a
# http://devfuria.com.br/python/built-in-enumerate/
#Tem q transformar pra string pra o enumerate percorrer
b = str(a)
for i, v in enumerate(b):
    # o V é os valores e o I éa  posição
   print(v)
  
#20
c1 = 0
l1 = []
c2 = 0
l2 = []
while True:
  n = (int(input('Numeros: ')))

  if n == 1000:
    break

  elif n % 2 == 0:
    l1.append(n)
    c1 += 1

  elif n % 2 != 0:
    l2.append(n)
    c2 += 1

print(f"Lista de numeros pares {l1} Quantos numeroes pares tem no total {c1}")
print(f"Lista de numeros impares {l2} Quantos numeroes impares tem no total {c2}")

#21
c1 = 0
l1 = []
c2 = 0
l2 = []
count = 0
mult =  1
while True:
    n = (int(input('Numeros: ')))
    if n == 1000:
        break
    if n % 2 == 0:
        l1.append(n)
        c1 +=1
        count += n
    else:
        l2.append(n)
        c2 += 1
        mult *= n

print(f"Lista de numeros pares {l1}\nQuantos numeroes pares tem no total {c1}\nQual a soma dos numeros pares {count}")
print(f"Lista de numeros impares {l2}\nQuantos numeroes impares tem no total {c2}\nQual a multiplicacao dos numeros impares {mult}")

#22
c = 0
s = 0
while True:
    n = (int(input('Numeros: ')))
    if (n >= 10 and n <= 20):
        c += 1
        s += n 
    else:
        print(f"Média: {s/c}")
        break
  
#23
n = (int(input('Numeros: ')))

for i in range (1, n):
    if n % i == 0:
        print(i)

#24
n = (int(input('Numeros: ')))
l = []
for i in range (1, n):
    if n % i == 0:
        l.append(i)
print(sum(l))

#25
soma3 = 0
soma5 = 0
for i in range (1000):
   if i % 3 == 0:
       soma3 += i

   elif i % 5 == 0:
       soma5 += i

print(f"soma dos multiplos de 3: {soma3}")
print(f"soma dos multiplos de 5: {soma5}")
print(f"soma total: {soma3 + soma5}")

#26
l1 = []
#n = (int(input('Numeros: ')))
#OU
#n = 0
while True:
  n += 1
  if (n % 11 == 0) or (n % 13 == 0) or (n % 17 == 0):
    l1.append(n)
    break

print(l1)

#27
n = (int(input('Numeros: ')))
l = []
for i in range(1, n+1):
    b = 1/i
    l.append(b)

h = 1 + sum(l)
print(f"H(n) = {h}")

#28
import math
n = (int(input('Numeros: ')))
l = []
l2 = []
for i in range(1, n+1):
  
    l.append(i)
    #Tem que importar a porra do MATCH se n se n multiplica os valores da lista
    N = math.prod(l[::-1])
  
    s = 1/N
    l2.append(s)
    
E = 1 + sum(l2)
print(f"E = {E}")

#29
import math
l1 = []
for i in range(1, 11):
    l1.append(i)
   
#o corno quer só para 5 termos então vai ser isso msm
S = 0 + (1/ math.prod(l1[1::-1])) + (2/ math.prod(l1[3::-1])) + (3/ math.prod(l1[5::-1])) + (4/ math.prod(l1[7::-1])) + (5/ math.prod(l1[9::-1]))

print(S)

#30
n = (int(input('Numeros: ')))
l1 = []
l2 = []
l3 = []
l4 = []

for i in range (1 , n+1, ):
    l1.append(i)
print(f"Operação 1: {sum(l1)}")

#NUM FAÇO MENOR KARALHA DE IDEIA DE COMO FAZER O 2
# FICO ASSIM
for i in range (1 , n+1):
    
    if i % 2 == 0:
        f = i - (2*i)
        l2.append(f)
        
    else:
        l3.append(i)

print(l2, l3)
f = sum(l3) + sum(l2)
print(f)

for i in range (1 , n+1, 2):
    l4.append(i)
print(f"Operação 3: {sum(l4)}")

#31
f = 0
for i in range (1, 100, 2):
    for x in range(1, 51):
        f += i/x
print(f)

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
  
#33
n = int(input("Numero: "))
i = int(input("Numero I: "))
j = int(input("Numero J: "))

for x in range (0, n+1):
   
   if (x % i == 0) or  (x % j == 0):
       print(x, end=",")

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
  
#35
l = []
n1 = int(input("Começo: "))
n2 = int(input("Fim: "))

if n1 > n2:
    print("Intervalo de Valores Invalidos")

else:
    for i in range(n1,n2+1):
        if i % 2 != 0:
            l.append(i)
            
print(sum(l))

#36
l1 = []
l2 = []
for i in range(1, 101):
    
    a = i ** 2
    l1.append(a)
    l2.append(i)

print(f"{sum(l2)**2} - {sum(l1)} = {(sum(l2)**2) - (sum(l1))} ")

#37
#PQP O DEVR DE CORNO MANSO DO KRL
# NUM TENHO 1 PUTO DE IDEIA DE COMO FAZ ESSE DAKI
#Peguei do gabarito da turma la
for i in range(1000, 10000):
    n1 = int(i.__str__()[0:2])
    n2 = int(i.__str__()[2:4])
    if (n1 + n2)**2 == i:
        print(i)

#38
#Peguei desse site aki
#https://rafaeljsouza.medium.com/100-dias-de-c%C3%B3digo-dia-8-projeto-euler-9-ea31c530a985
A = 0
B = 0
C = 0 
#0 até mil
for c in range (0,1000):
    # de 0 até mill MENOS o valor q c escolheu
    for b in range(0, 1000-c):
        #de 0 até 1 valor abaixo de b
        for a in range(0, b):
            if a + b + c ==1000 and a**2 + b**2 == c**2:
                A += a
                B += b
                C += c

print(A, B, C)

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

#40
l = []
t = True
while t:
    n = int(input("Numero: "))
    if n < 0:
        print(max(l), min(l))
        t = False
        break
    else:
        l.append(n)

#41
t = True

while t :
    r1 = int(input("R1:"))
    r2 = int(input("R2:"))

    R = (r1*r2) / (r1+r2)

    if (r1 & r2) == 0 or R == 0:
        print("R = 0")
        t = False

    else:
        print(R)
  
#42
while True:
    n = int(input("Numero: "))
    if n <= 0:
        print('Fim')
        False
        break
        
    else:
        print((n**2), (n**3), (n**0.5))
  
#43
c = 0
l = []
while True:
    n = int(input("Idade: "))
    l.append(n)
    c += 1
    if n == 0:
        print(f"Média: {(sum(l))/c}")
        False
        break

#44
#https://www.delftstack.com/pt/howto/python/fibonacci-sequence-python/
n = int(input("Numero: "))

a=1
b=1
if n==1:
    print('0')
elif n==2:
    print('0','1')
else:
    print('0')
    print(a)
    print(b)
    for i in range(n-3):
        total = a + b
        b=a
        a= total
        print(total)

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

#46
import random
a = random.randint(1,1000)

while True:
    n = int(input("Numero: "))

    if n > a:
        print("Valor mais alto que A, ABAIXA")
    elif n < a:
        print("Valor mais baixo que A, AUMENTA")
    else:
        print("Acerto")
        False
        break
  
#47
n1 = int(input("N1: "))
n2 = int(input("N2: "))

while True:
    o = int(input(
    "\n1 - Adição\n" 
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão\n"
    "5 - Saida\n"
    "Qual tu escolhe: ""\n"))

    if o == 1:
        print(n1+n2)

    elif o == 2:
        print(n1-n2)
    
    elif o == 3:
        print(n1*n2)
    
    elif o == 4:
        print(n1/n2)

    elif o == 5:
        print("Cabou")
        False
        break
  
#48
# https://franciscochaves.com.br/blog/fibonacci-em-python
anterior = 0
proximo = 0

n = int(input("Numero: "))

while(proximo < n):
    proximo = proximo + anterior
    anterior = proximo - anterior
    proximo += proximo

    if proximo > 4*(10**6):
        False
        break

print(proximo)

#49
carlos = float(input("Qual teu salario: "))
joao = carlos/3

meses = 0

while True:
    p_carlos = (2*carlos)/100
    p_joao = (5*joao)/100
    meses += 1
    carlos += p_carlos
    joao += p_joao

    if joao > carlos:
        print(meses," Meses")
        False
        break

#50
chico = 1.50
ze = 1.10
ano = 0

while True:
    c_chico = 0.02
    c_ze = 0.03
    ano += 1
    chico += c_chico
    ze += c_ze

    if ze > chico:
        print(ano," Anos")
        False
        break

#51
funcionario = 2000
ano = 1995

while ano < 2022:
    ano += 1
    aumento = (1.5*funcionario)/100
    funcionario += aumento
    
    if ano == 1997:
        while True:
            ano += 1
            funcionario += (2*aumento)
            

            if ano == 2022:
                False
                break

print(ano, funcionario)

#52
# https://www.clubedohardware.com.br/forums/topic/1395636-python-algoritmo-de-caixa-eletr%C3%B4nico/
saque = int(input('Digite o valor do saque: '))
total = saque #Montante total que será decomposto
nota = 100 #Tirar 100 reais do montante
totalnotas = 0
while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print('Total de {} notas de R$ {}' .format(totalnotas, nota))
        if nota == 100:
            nota = 50
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        totalnotas = 0
        if total == 0:
            break

#53
#https://pt.stackoverflow.com/questions/467071/como-deixar-as-colunas-do-tri%C3%A2ngulo-de-floyd-perfeitamente-sim%C3%A9tricas
n = int(input(f'Digite o número de linhas: '))

m = 1
for c in range(1, n + 1):
    for i in range(1, c + 1):
        print(f'{m:<4}', end='')
        m += 1
    print()

#54
# https://acervolima.com/programa-python-para-verificar-se-um-numero-e-primo-ou-nao/
num = int(input("Numero: "))
 
if num > 1:
    
    for i in range(2, num):
      
        if (num % i) == 0:
            print(num, "Primo")
            break
    else:
        print(num, "primo")
 
else:
    print(num, "Não Primo")

#55
# https://pt.stackoverflow.com/questions/454612/a-soma-dos-n-primeiros-n%C3%BAmeros-primos
n = int(input('Digite um número inteiro positico: '))
soma = 0

for num in range(2, n + 1):
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        print(num)
        soma += num

print(soma)

#56
n = 2000000

soma = []

for num in range(2, n):
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        print(num)
        soma.append(num)
        
print(sum(soma))

#57
n1 = int(input('número 1: '))
n2 = int(input('número 2: '))

soma = []

for num in range(n1, n2+1):
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        soma.append(num)
        
print(len(soma))

#58
n1 = int(input('número 1: '))
n2 = int(input('número 2: '))

soma = []

for num in range(n1, n2+1):
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        soma.append(num)
        
print(sum(soma))

#59
#MANO ESSE NOIA NUM SABE ESCREVER, ele pediu N de habitantes pra Q?
# Ele nem passo a regra, sorte que eu achei o enunciado e a regra na net
# https://python.nilo.pro.br/exercicios3/capitulo%2004/exercicio-04-10.html
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
'''''
+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
'''''
consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
if tipo == "R":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço
print(f"Valor a pagar: R$ {custo:7.2f}")

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

#61
# https://pt.stackoverflow.com/questions/226102/encontrar-o-maior-pal%C3%ADndromo-feito-a-partir-do-produto-de-dois-n%C3%BAmeros-de-3-d%C3%ADgi
i = 0
j = 0
pol = 0
while i <= 999:
    j = i
    while j <= 999:
        temp = str(i * j)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            polTemp = int(temp)
            if polTemp > pol:
                pol = polTemp
        j += 1
    i += 1
print(pol)

#62
#VAI SE FUDE ESSA QUESTÃO AKI
#ESSA PORRA FOI REMOVIDA DO GABARITO DO CARA LA
"""
pip install num2words
from num2words import num2words
 
total = ""
 
for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    total += num.replace(' ', '')
 
print(f'Entre 1 e 1000 temos {len(total)} letras.')
"""