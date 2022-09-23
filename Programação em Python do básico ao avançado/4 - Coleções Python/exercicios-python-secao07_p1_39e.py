#1 
v = []
#A)
v.append(1)
v.append(0)
v.append(5)
v.append(-2)
v.append(-5)
v.append(7)
#B)
s = v[0] + v[1] + v[5]
print(s)
#C)
v[4] = 100
print(v)
#D)
for i in v:
    print(i)

#2
l = [1, 2, 3, 4, 5, 6]
print( *l, sep=', ')

#3
l = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1]
c = []
for i in l:
    a = i*i
    c.append(round(a,2))
print("Conjunto Inicial")
print(l)
print("Conjunto Final")
print(c)

#4
l = [1, 2, 3, 4, 5, 6, 7, 8]
print("Posição 2 ==" , l[2], "\n"  + 
"Posição 6 ==", l[6], "\n" +
"Soma ==", l[2] + l[6])

#5
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = []
for i in l:
    if i % 2 == 0:
        p.append(i)

print("Possui", len(p), "valores pares")
print("Lista dos Valores")
print( *p, sep=', ')

#6
l = []
for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

print("Maior Valor ==", max(l))
print("Menor Valor ==", min(l))

#7
l = []
for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

print(l)
print("Valor Maior:",max(l), "Posição:",l.index(max(l)))

#8
l = []

for i in range(1,7):
    a = int(input("Valor: "))
    l.append(a)

print(l)
print("Ordem Inversa")
print(l[::-1])

#9
l = []
p = []
for i in range(1,7):
    a = int(input("Valor: "))
    l.append(a)

for i in l:
    if i % 2 == 0:
        p.append(i)

print("Ordem Inversa")
print(p[::-1])

#10
l = [1,2,3,4,5,6,7,8]

for i in range(1,16):
    a = float(input("N: "))
    # Não falou até quanto era a nota, então n botei tratamento
    l.append(a)

media = sum(l)/len(l)
print("Média das Notas:",round(media,2))

#11
l = []
p = []
I = []

for i in range(1,11):
    a = float(input("N: "))
    l.append(a)

for i in l:
    if i > 0:
        p.append(i)
    elif i < 0:
        I.append(i)

print("Quantidade de Negativos ==",len(I))
print("Soma dos Positivos ==", sum(p))

#12
l = []

for i in range(1,6):
    a = float(input("N: "))
    l.append(a)

media = sum(l)/len(l)
print("Maior:", max(l), "Menor:", min(l), "Média:", media)

#13
l = []

for i in range(1,6):
    a = float(input("N: "))
    l.append(a)

print("Posição do Maior:",l.index(max(l)))
print("Posição do Menor:",l.index(min(l)))

#14
from collections import Counter
l = []

for i in range(1,11):
    a = float(input("N: "))
    l.append(a)

c = Counter(l)

print("Numero : VZ de Repetição")
print(c)

#15
l = []

for i in range(1,21):
    a = int(input("N: "))
    l.append(a)

print(l)
print("Eliminando elementos repetidos")
print(sorted(set(l)))

#16
l1 = []
l2 = []

for i in range(1,6):
    a = int(input("Valor: "))
    l1.append(a)
    l2.append(float(a))

print("\n0 - cabo\n"
"1 - Print\n"
"2 - Ordem invertida\n")

while True:
    escolha = int(input("Escolha: "))

    if escolha == 0:
        exit
        False
        break

    elif escolha == 1:
        print(l1,"\n")
        print(l2)
        False 
        break

    elif escolha == 2:
        print(l1[::-1],"\n")
        print(l2[::-1])
        False 
        break

    else:
        print("Codigo Invalido")

#17
l = []

for i in range(1,6):
    a = int(input("Valor: "))
    l.append(a)

print(l,"\n")

ind = [] # 1° descobrir os negativos
for i in l:    
    if i < 0:
        ind.append(i)

indx = [] # descobrir os indices dos negativos
for i in ind:
    indx.append(l.index(i))

for i in indx: # resolver
    del(l[i])
    l.insert(i,0)
# ESSA PORRA LEVO TEMPO P KRL
print(l)

#18
l = [*range(1,11)]
print(l)

n1 = int(input("Escolha 1 nuemro da lista: "))
n2 = max(l)

mult = []
count = 0
for c in range(n1, n2+1):
    if c % n1 == 0:
        mult.append(c)
        count += 1
print('O numero {} tem os multiplos {} no total tem {} multiplos'.format(n1, mult, count))

#19
l = [*range(1,51)]
l2 = []

for i in l:
    a = (i + 5 * i) / (i + 1)
    l2.append(round(a,2))

print(l2)

#20
# ESTE AKI FOI 1 PUTA CODIGO DE CORNO QUE EU N FAZIA IDEIA DE COMO FAZER
# PEGUEI DAKI
# https://brainly.com.br/tarefa/37911702
def mostra_vetor (lst) :
    cont = 0
    while True:
        try :
            print(lst [cont], end=" ")

            cont += 1
            if cont%2 == 0:
                print( )
        except:
            break

Ist_int = list()
Ist_impares = list()
print(' Envie 10 numeros inteiros no intervalo fechado [0, 50]')

for i in range(10) :
    while True:
        try :
            num = int(input(f"Digite o {i+1} numero: "))

            if 0 <= num <= 50:
                Ist_int. append(num)
                break
            else:
                print('Entrada invalida! 0 numero deve estar no intervalo [0, 50]')
                continue
        except:
            print('Entrada invalida! Digite um numero inteiro no intervalo [0,50]')

for numero in Ist_int:
    if numero%2 != 0:
        Ist_impares . append(numero)

print('\nPrimeiro vetor: ' )
mostra_vetor (Ist_int)
print ("\nSegundo vetor vetor: ")
mostra_vetor(Ist_impares)

#21
A = []
B = []

for i in range(1,11):
    a = int(input("Valor A: "))
    b = int(input("Valor B: "))
    A.append(a)
    B.append(b)

indA = [] 
for i in A:
    indA.append(A.index(i))

indB = [] 
for i in B:
    indB.append(B.index(i))

C = []

for a in indA:
    for b in indB:
        c = A[a] - B[b]
    C.append(c)

print(C)

#22
A = []
B = []

for i in range(1,11):
    a = int(input("Valor A: "))
    b = int(input("Valor B: "))
    A.append(a)
    B.append(b)

pares = []
impares = []

for x in A:
    if x % 2 == 0:
        pares.append(x)

    elif x % 2 != 0:
        impares.append(x)

for y in B:
    if y % 2 == 0:
        pares.append(y)

    elif y % 2 != 0:
        impares.append(y)
    
print("Lista de Pares", pares)
print("Lista de Impares",impares)

#23
A = []
B = []

for i in range(1,6):
    a = float(input("Valor A: "))
    b = float(input("Valor B: "))
    A.append(a)
    B.append(b)

produto_escalar = []

for x in A:
    for y in B:
        p = x * y
    produto_escalar.append(p)
    
print("Produto Escalar =",sum(produto_escalar))

#24
alunos = {}

c = 0

while True:

    id = int(input("Id do Aluno: "))

    if alunos.get(id):
        print("Ja existe o ID ", id)
        
    else:
        h = float(input("H do Aluno: "))
        alunos[id] = h
        c += 1

    if c == 3:
        False
        break

max_key = max(alunos, key = alunos.get)
max_value = alunos.get(max_key)

min_key = min(alunos, key = alunos.get)
min_value = alunos.get(min_key)

print("Id do aluno mais alto:", max_key, "\n"
"altura:", max_value, "\n"
"Id do aluno mais baixo:", min_key, "\n"
"altura do aluno mais baixo:", min_value)

#25
# To ficando sem saco já
l = []

for i in range(1,101):
    print(i)
    if i % 7 != 0:
        l.append(i)

print(l)

#26
# https://www.delftstack.com/pt/howto/python/standard-deviation-of-a-list-in-python/
# https://acervolima.com/calcule-a-media-variancia-e-desvio-padrao-em-python-usando-numpy/#:~:text=Desvio%20padr%C3%A3o%20em%20Python%20usando%20Numpy%3A%20Pode-se%20calcular,padr%C3%A3o%20usando%20a%20fun%C3%A7%C3%A3o%20numpy.std%20%28%29%20em%20python.
import numpy as np

list = [*range(1,11)]
print("List : " + str(list))

st_dev = np.std(list)

print("Standard deviation of the given list: " + str(st_dev))

#27
# https://acervolima.com/programa-python-para-verificar-se-um-numero-e-primo-ou-nao/
l = []

for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

primos = []
N_primos = []

for num in l:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                #print(num, "is not a prime number")
                N_primos.append(num)
                break
        else:
            #print(num, "is a prime number")
            primos.append(num)
    
    else:
        #print(num, "is not a prime number")
        N_primos.append(num)

inds = []
for i in primos:
    inds.append(l.index(i))

print("Numeros primos:", primos)
print("Posição dos numeros primos na lista", inds)

#28
l = []

for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

v1 = []
v2 = []

for x in l:
    if x % 2 == 0:
        v2.append(x)

    elif x % 2 != 0:
        v1.append(x)
    
print("Lista de Pares", v2)
print("Lista de Impares", v1)

#29
l = []

for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

v1 = []
v2 = []

for x in l:
    if x % 2 == 0:
        v2.append(x)

    elif x % 2 != 0:
        v1.append(x)

print("Lista de Pares", v2)
print("soma dos pares", sum(v2))
print("Lista de Impares", v1)
print("Quantidade de impares", len(v1))

#30
l1 = []
l2 = []
l3 = []

c1 = 0
c2 = 0

print("1° Lista \n")
while True:
    a = int(input("Valor da 1° lista: "))
    if a not in l1:
        l1.append(a)
        c1 +=1
    else:
        print("Não pode Valor repetido")

    if c1 == 10:
        False
        break

print("\n2° Lista")
while True:
    b = int(input("Valor da 2° lista: "))
    if b not in l2:
        l2.append(b)
        c2 +=1
    else:
        print("Não pode Valor repetido")

    if c2 == 10:
        False
        break
    
for x in l1: 
    for y in l2:
        if x == y:
            l3.append(x)

print("1° Lista:", l1)
print("2° Lista:", l2)
print("Valores em comum",l3)

#31
l1 = []
l2 = []

c1 = 0
c2 = 0

print("1° Lista \n")
while True:
    a = int(input("Valor da 1° lista: "))
    if a not in l1:
        l1.append(a)
        c1 +=1
    else:
        print("Não pode Valor repetido")

    if c1 == 10:
        False
        break

print("\n2° Lista")
while True:
    b = int(input("Valor da 2° lista: "))
    if b not in l2:
        l2.append(b)
        c2 +=1
    else:
        print("Não pode Valor repetido")

    if c2 == 10:
        False
        break
    
l3 = set(l1 + l2)

print("1° Lista:", l1)
print("2° Lista:", l2)
print("Valores unidos", l3)

#32
l1 = []
l2 = []

c1 = 0
c2 = 0

print("1° Lista \n")
while True:
    a = int(input("Valor da 1° lista: "))
    if a not in l1:
        l1.append(a)
        c1 +=1
        
    else:
        print("Não pode Valor repetido")

    if c1 == 5:
        False
        break


print("\n2° Lista")
while True:
    b = int(input("Valor da 2° lista: "))
    if b not in l2 and b not in l1:
        l2.append(b)
        c2 +=1
    else:
        print("Não pode Valor repetido e nem valor da 1° lista")

    if c2 == 5:
        False
        break

print("1° Lista:", l1)
print("2° Lista:", l2)
#A
# https://pt.stackoverflow.com/questions/309189/soma-de-cada-elemento-de-duas-listas
soma = [ (a + b) for a, b in zip(l1, l2) ]
print("Soma", soma)
#B
# https://www.delftstack.com/pt/howto/python/multiply-two-lists-python/
multi = [ (a * b) for a, b in zip(l1, l2) ]
print("Multiplicação", multi)
#C
difenc = [ (a - b) for a, b in zip(l1, l2) ]
print("Diferença", difenc)
#D
l3 = []
for x in l1: 
    for y in l2:
        if x == y:
            l3.append(x)
print("Valores em comum", l3)
#E
unir = set(l1 + l2)
unidos = list(unir)
print(unidos)

#33
#https://stackoverflow.com/questions/49973739/python-how-to-remove-zeroes-from-a-list-in-python
l = []
for i in range(0,15):
    a = int(input("N: "))
    l.append(a)

X = [i for i in l if i != 0]
print(X)

#34
l1 = []
c1 = 0

print("Lista \n")
while True:
    a = int(input("Valor da lista: "))
    if a not in l1:
        l1.append(a)
        c1 +=1
    else:
        print("Não pode Valor repetido")

    if c1 == 10:
        False
        break
print(l1)

#35
# ESSA PORRA DE QUESTÃO É CONFUSA P KRL, NÃO FAZ SENTIDO
# A PROXIMA POSIÇÃO SEMPRE VAI SER A ANTERIOR MAIS 1,
# E ELE NÃO DA PARAMETRO DE INICIO
# VAI A MERDA ESSA QUESTÃO

#36 37 38
# AS 3 SÃO SÓ DE ORDEM, ENTÃO FDC
l = []
for i in range(1,12):
    a = int(input("N: "))
    l.append(a)

l = sorted(l)
print("Ordem Crescente", l)
print("Ordem Inversa", l[::-1])

#39
# https://www.delftstack.com/es/howto/python/python-pascal-triangle/#:~:text=Para%20formar%20un%20tri%C3%A1ngulo%20pascal%20en%20Python%2C%20hay,lista%20vac%C3%ADa%2C%20que%20se%20utiliza%20para%20almacenar%20valores.
num = int(input("Enter the number of rows:"))
for n in range(num):
    print(''*(num-n), end='')

    print(''.join(map(str, str(11**n))))
#VAI SE FUDER ESSE DEVER
