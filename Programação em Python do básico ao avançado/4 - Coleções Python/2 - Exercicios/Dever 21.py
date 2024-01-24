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