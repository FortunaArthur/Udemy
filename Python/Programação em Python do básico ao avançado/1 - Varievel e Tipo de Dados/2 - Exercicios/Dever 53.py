#53
c = float(input("Comprimento: "))
l = float(input("Largura: "))
p = float(input("Preço por metro de rede: "))

formula = c*l
formula = formula**2
formula = formula*p

print(f"Vai custar {formula} pra redear td terreno")