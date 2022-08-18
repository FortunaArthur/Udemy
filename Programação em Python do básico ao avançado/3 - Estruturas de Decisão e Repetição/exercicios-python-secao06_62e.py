#1
# for i in rane (inicio, fim, incremento(Que vai  pulando))
from tokenize import Ignore


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
