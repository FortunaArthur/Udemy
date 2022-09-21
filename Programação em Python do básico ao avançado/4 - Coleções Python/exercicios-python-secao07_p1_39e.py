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
    a = float(input("Nota: "))
    # Não falou até quanto era a nota, então n botei tratamento
    l.append(a)

media = sum(l)/len(l)
print("Média das Notas:",round(media,2))

#11
l = []
p = []
I = []

for i in range(1,11):
    a = float(input("Nota: "))
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
    a = float(input("Nota: "))
    l.append(a)

media = sum(l)/len(l)
print("Maior:", max(l), "Menor:", min(l), "Média:", media)

#13
l = []

for i in range(1,6):
    a = float(input("Nota: "))
    l.append(a)

print("Posição do Maior:",l.index(max(l)))
print("Posição do Menor:",l.index(min(l)))

