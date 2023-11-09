#16
n = int(input("Numerode 1 a 12: "))

m = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

if n >= 1 and n <= 12:
    for i in m:
        if n == i:
            print(m[i])
else:
    print("Valor invalido")