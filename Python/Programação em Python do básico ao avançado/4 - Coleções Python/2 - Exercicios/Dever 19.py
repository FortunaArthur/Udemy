#19
l = [*range(1,51)]
l2 = []

for i in l:
    a = (i + 5 * i) / (i + 1)
    l2.append(round(a,2))

print(l2)