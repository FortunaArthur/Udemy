#37
#PQP O DEVR DE CORNO MANSO DO KRL
# NUM TENHO 1 PUTO DE IDEIA DE COMO FAZ ESSE DAKI
#Peguei do gabarito da turma la
for i in range(1000, 10000):
    n1 = int(i.__str__()[0:2])
    n2 = int(i.__str__()[2:4])
    if (n1 + n2)**2 == i:
        print(i)