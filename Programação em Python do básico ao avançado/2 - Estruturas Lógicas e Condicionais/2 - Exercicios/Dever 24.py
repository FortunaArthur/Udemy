#24
n = float(input("Qul o valor do produto: "))
print("Imposto sobre o produto por estado" + "\n"
"MG : 07%" + "\n"
"SP : 12%" + "\n"
"RJ : 15%" + "\n"
"MS : 08%" + "\n")
i = input("Pra qual estado o produto será enviado: ").upper()

if i == "MG":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 7) / 100)}")

elif i == "SP":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 12) / 100)}")

elif i == "RJ":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 15) / 100)}")

elif i == "MS":
    print(f"Preço do produto: {n}, preço + imposto do estado { n + ((n * 8) / 100)}")

else:
    print("Erro de estado")