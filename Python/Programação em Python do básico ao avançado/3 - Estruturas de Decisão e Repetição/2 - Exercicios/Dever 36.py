#36
l1 = []
l2 = []
for i in range(1, 101):

    a = i ** 2
    l1.append(a)
    l2.append(i)

print(f"{sum(l2)**2} - {sum(l1)} = {(sum(l2)**2) - (sum(l1))} ")