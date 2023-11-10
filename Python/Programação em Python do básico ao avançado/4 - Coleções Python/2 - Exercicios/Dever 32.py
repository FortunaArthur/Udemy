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