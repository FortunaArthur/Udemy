#36
n = float(input("Qual o valor da venda mensal: "))

f = round((( n * 14) / 100))

if n < 20000 :
    print(f"Comissão: {400 + f}")
else:
    if n >= 20000 and n < 40000:
        print(f"Comissão: {500 + f}")
    else:
        if n >= 40000 and n < 60000:
            print(f"Comissão: {550 + f}")
        else:
                if n >= 60000 and n < 80000:
                    print(f"Comissão: {600 + f}")
                else:
                    if n >= 80000 and n < 100000:
                        print(f"Comissão: {650 + f}")
                    else:
                        if n > 100000:
                            print(f"Comissão: {600 + round((( n * 16) / 100))}")