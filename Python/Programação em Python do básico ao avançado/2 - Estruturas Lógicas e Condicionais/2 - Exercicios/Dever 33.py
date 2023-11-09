#33
n = float(input("Preço do produto: "))

if n <= 50:
    f = n + ((n * 5) / 100)
    if f <= 80:
        print("Barato")

if n > 50 and n1 <= 100:
    f = n + ((n * 10) / 100)
    if f > 80 and f <= 120:
        print("Normal")

if n > 100:
    f = n + ((n * 15) / 100)
    if f > 120 and f <= 200:
        print("Caro")
    elif n > 200:
        print("Caro p krl")

else:
    print("Erro")