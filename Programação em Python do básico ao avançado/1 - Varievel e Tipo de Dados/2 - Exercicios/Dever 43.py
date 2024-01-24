#43
n = float(input("Qual o preço total?: "))
formula1 = n - (n*10/100)
formula2 = n / 3
formula3 = (n*5/100)
formula4 = (formula2*5/100)
print(f"Total: {formula1}")
print(f"Parcela dividido por 3: {formula2}")
print(f"Comissão do vendedor caso a venda seja a vista: {formula3}")
print(f"Comissão do vendedor no caso de ser parcelado: {formula4}")