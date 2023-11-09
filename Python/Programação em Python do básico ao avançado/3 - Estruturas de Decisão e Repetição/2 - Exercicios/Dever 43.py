#43
c = 0
l = []
while True:
    n = int(input("Idade: "))
    l.append(n)
    c += 1
    if n == 0:
        print(f"Média: {(sum(l))/c}")
        False
        break