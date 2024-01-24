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