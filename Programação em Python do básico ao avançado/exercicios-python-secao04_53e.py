def Pular_Linha():
    pular_linha = "\n"*2
    print(pular_linha)
'''''''''''''''''''''''
#1
n = int(input("numero inteiro: "))
print(n, type(n))
Pular_Linha()

#2
n = float(input("numero real(float): "))
print(n, type(n))
Pular_Linha()

#3
print("Digita ai 3 numero inteiro :")
n1 = int(input('N1: '))
n2 = int(input("N2: "))
n3 = int(input("N3: "))
print(f"A SOMA DOS 3 é igual a : {n1+n2+n3} ")
Pular_Linha()

#4
n = float(input("Nuemro real(float): "))
print(f"O  valor {n}² é igual a : {n**2}")
Pular_Linha()

#5
n = float(input("Numero real(float): "))
print(f"A Kinta parte de {n} é igual a {n/5}")
Pular_Linha()

#6
n = float(input("Digita 1 temperatura ai: "))
formula = n*(9/5)+32
print(f"Convertida de Celsius pra Fahrenheit: {formula}")
Pular_Linha()

#7
n = float(input("Digita 1 temperatura ai: "))
formula = 5*(n-32)/9
print(f"Convertida de Fahrenheit pra Celsius: {formula}")
Pular_Linha()

#8
n = float(input("Digita 1 temperatura ai: "))
formula = n - 273.15
print(f"Convertida de Kelvin pra Celsius: {formula}")
Pular_Linha()

#9
n = float(input("Digita 1 temperatura ai: "))
formula = n + 273.15
print(f"Convertida de Celsius pra Kelvin {formula}")
Pular_Linha()

#10
n = float(input("Digita 1 velocidade ai: "))
formula = n/3.6
print(f"Era {n}KM/H e ficou {formula}M/S")
Pular_linha()

#11
n = float(input("Digita 1 velocidade ai: "))
formula = n * 3.6
print(f"Era {n}M/S e ficou {formula}KM/H")
Pular_Linha()

#12
n = float(input("Digita 1 velocidade ai: "))
formula = n / 1.61
print(f"Era {n} Milhas e ficou {formula}KM")
Pular_Linha()

#13
n = float(input("Digita 1 velocidade ai: "))
formula = 1.61 * n
print(f"Era {n}KM e ficou {formula} Milhas")
Pular_Linha()

#14
n = float(input("Digite 1 angulo ai: "))
formula = n * (3.14/180)
print(f"Era {n}°Graus e em radianos ficou {formula}")
Pular_Linha()

#15
n = float(input("Digite 1 angulo ai: "))
formula = n * (180/3.14)
print(f"Era {n} Radianos e em Graus ficou {formula}")
Pular_Linha()

#16
n = float(input("Digite 1 valor ai: "))
formula = n * 2.54
print(f"Era {n} polegadas e em centimetros ficou {formula}")
Pular_Linha()

#17
n = float(input("Digite 1 valor ai: "))
formula = n / 2.54
print(f"Era {n} centimetros e em polegadas ficou {formula}")
Pular_Linha()

#18
n = float(input("Digite 1 valor ai: "))
formula = 1000 * n
print(f"Era {n} metros cubicos e em litros ficou {formula}")
Pular_Linha()

#19
n = float(input("Digite 1 valor ai: "))
formula = n/1000
print(f"Era {n} litros e em metros cubicos ficou {formula}")
Pular_Linha()

#20
n = float(input("Digite 1 valor ai: "))
formula = n/0.45
print(f"Era {n} quilogramas e em libras ficou {formula}")
Pular_Linha()

#21
n = float(input("Digite 1 valor ai: "))
formula = n * 0.45
print(f"Era {n} libras e em quilogramas ficou {formula}")
Pular_Linha()

#22
n = float(input("Digite 1 valor ai: "))
formula = 0.91 * n
print(f"Era {n} jardas e em metros ficou {formula}")
Pular_Linha()

#23
n = float(input("Digite 1 valor ai: "))
formula = n/0.91
print(f"Era {n} metros e em jardas ficou {formula}")
Pular_Linha()

#24
n = float(input("Digite 1 valor ai: "))
formula = n * 0.000247
print(f"Era {n} metros quadrados e em acres ficou {formula}")
Pular_Linha()

#25
n = float(input("Digite 1 valor ai: "))
formula = n * 4048.58
print(f"Era {n} acres e em metros quadrados ficou {formula}")
Pular_Linha()

#26
n = float(input("Digite 1 valor ai: "))
formula = n * 0.0001
print(f"Era {n} metros quadrados e em hectares ficou {formula}")
Pular_Linha()

#27
n = float(input("Digite 1 valor ai: "))
formula = n * 10000
print(f"Era {n} hectares e em metros quadrados ficou {formula}")
Pular_Linha()

#28
print("Digite 3 numeros ai")
n1 = float(input("N1: "))
n2 = float(input("N2: "))
n3 = float(input("N3: "))
print(f"Os valores {n1, n2, n3} tem os quadrados {n1**2, n2**2, n3**2} e a soma de seus quadrados é {n1**2 + n2**2 + n3**2}")
Pular_Linha()

#29
print("Digita ai a lastima das notas de teu aluno")
n1 = float(input("N1: "))
n2 = float(input("N2: "))
n3 = float(input("N3: "))
n4 = float(input("N4: "))
formula = (n1+n2+n3+n4)/4
print(f"A média das notas é {formula}")
Pular_Linha()

#30
#cotação do dolar dia 03/08/2022 é 5,27
n = float(input("Digita quando vc tem em REAL e boa sorte: "))
formula = n / 5.27
print(f"Vc tem {n}R$ e em dolar vc tem {formula}$")
Pular_Linha() 
'''''''''''''''''''''''''''
#31
n = int(input("Digita 1 numero ai: "))
print(f"Antecessor: {n-1}, Sucessor: {n+1}")
Pular_Linha()

#32
n = int(input("Digita 1 numero ai: "))
print(f"Antecessor: {n-1}, Sucessor: {n+1}")
print(f"Triplo do Sucessor: {(n+1)*3}, Dobro do Antecessor: {(n-1)*2}")
print(f"Soma: {((n+1)*3) + ((n-1)*2) }")
Pular_Linha()

#33
n = int(input("Digita 1 numero ai: "))
print(f"Area do quadrado: {n**2}")
Pular_Linha()

#34
n = float(input("Digita 1 numero ai: "))
print(f"Area do circulo: {3.141592 * (n**2)}")
Pular_Linha()

#35
print("Fudeu, questão de ensino medio, calcular hipotenuza")
n1 = float(input("A: "))
n2 = float(input("B: "))
formula = ((n1**2) + (n2**2)) ** 0.5
print(f"Resultado: {formula}")
Pular_Linha()

#36
print("Porra, outra questão de ensino medio, calcular volume de cilindro")
n1 = float(input("Raio: "))
n2 = float(input("Altura: "))
formula = (3.141592 * (n1**2)) * n2
print(f"Resultado: {formula}")
Pular_Linha()

#37
n = float(input("Valor do produto: "))
print(f"Valor + desconto: {((n*12)/100) - n}")
Pular_Linha()

#38
n = float(input("Salario: "))
print(f"Salario + aumennto: {((n*25)/100) + n}")
Pular_Linha()

#39

