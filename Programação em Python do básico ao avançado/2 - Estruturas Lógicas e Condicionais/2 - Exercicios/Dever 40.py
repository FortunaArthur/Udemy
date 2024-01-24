#40
#Só falatav esse e fikei sem saco pra escerver
#peguei daki
#https://gist.github.com/AlyoshaS/0126ca3dd672c2d5fb04fac0261dd600

custo_fabrica = float(input("Digite o custo de fábrica: "))

if custo_fabrica <= 12000:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.05)))
elif custo_fabrica <= 25000:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.10) + (custo_fabrica * 0.15)))
else:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.20)))