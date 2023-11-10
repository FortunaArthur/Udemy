#12
l = []

for i in range(1,6):
    a = float(input("N: "))
    l.append(a)

media = sum(l)/len(l)
print("Maior:", max(l), "Menor:", min(l), "Média:", media)