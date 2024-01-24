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