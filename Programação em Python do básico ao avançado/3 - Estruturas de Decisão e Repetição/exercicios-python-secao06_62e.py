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

