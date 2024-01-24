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