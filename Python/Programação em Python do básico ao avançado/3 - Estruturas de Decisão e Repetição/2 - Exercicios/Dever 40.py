#40
l = []
t = True
while t:
    n = int(input("Numero: "))
    if n < 0:
        print(max(l), min(l))
        t = False
        break
    else:
        l.append(n)