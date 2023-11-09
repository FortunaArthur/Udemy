#22
c = 0
s = 0
while True:
    n = (int(input('Numeros: ')))
    if (n >= 10 and n <= 20):
        c += 1
        s += n
    else:
        print(f"Média: {s/c}")
        break