#10
l = []

for i in range(1,16):
    a = float(input("N: "))
    # Não falou até quanto era a nota, então n botei tratamento
    l.append(a)

media = sum(l)/len(l)
print("Média das Notas:",round(media,2))