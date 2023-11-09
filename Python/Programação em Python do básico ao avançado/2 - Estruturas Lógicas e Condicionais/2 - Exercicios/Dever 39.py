#39
n = float(input("Qual teu salario: "))
a = float(input("Quantos anos vc trampou: "))

if n <= 500:
    f = round((( n * 25) / 100))
    if n < 1:
        print(f"Seu salario é: {f + n}")

    if a >= 1 and a <= 3:
        print(f"Seu salario é: {(f + n) + 100}")

    if a >= 4 and a <= 6:
        print(f"Seu salario é: {(f + n) + 200}")

    if a >= 7 and a <= 10:
        print(f"Seu salario é: {(f + n) + 300}")

    if a > 10:
        print(f"Seu salario é: {(f + n) + 500}")

elif n <= 1000:
    f = round((( n * 20) / 100))
    if n < 1:
        print(f"Seu salario é: {f + n}")

    if a >= 1 and a <= 3:
        print(f"Seu salario é: {(f + n) + 100}")

    if a >= 4 and a <= 6:
        print(f"Seu salario é: {(f + n) + 200}")

    if a >= 7 and a <= 10:
        print(f"Seu salario é: {(f + n) + 300}")

    if a > 10:
        print(f"Seu salario é: {(f + n) + 500}")

elif n <= 1500:
    f = round((( n * 15) / 100))
    if n < 1:
        print(f"Seu salario é: {f + n}")

    if a >= 1 and a <= 3:
        print(f"Seu salario é: {(f + n) + 100}")

    if a >= 4 and a <= 6:
        print(f"Seu salario é: {(f + n) + 200}")

    if a >= 7 and a <= 10:
        print(f"Seu salario é: {(f + n) + 300}")

    if a > 10:
        print(f"Seu salario é: {(f + n) + 500}")

elif n <= 2000:
    f = round((( n * 10) / 100))
    if n < 1:
        print(f"Seu salario é: {f + n}")

    if a >= 1 and a <= 3:
        print(f"Seu salario é: {(f + n) + 100}")

    if a >= 4 and a <= 6:
        print(f"Seu salario é: {(f + n) + 200}")

    if a >= 7 and a <= 10:
        print(f"Seu salario é: {(f + n) + 300}")

    if a > 10:
        print(f"Seu salario é: {(f + n) + 500}")

elif n > 2000 :
    if n < 1:
        print(f"Seu salario é: {n}")

    if a >= 1 and a <= 3:
        print(f"Seu salario é: {(n) + 100}")

    if a >= 4 and a <= 6:
        print(f"Seu salario é: {(n) + 200}")

    if a >= 7 and a <= 10:
        print(f"Seu salario é: {(n) + 300}")

    if a > 10:
        print(f"Seu salario é: {(n) + 500}")

else:
    print("Valores errados")