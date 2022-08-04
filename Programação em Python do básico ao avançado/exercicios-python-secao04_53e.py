def Pular_Linha():
    pular_linha = "\n"*2
    print(pular_linha)

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
Pular_Linha()

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
print(f"Valor + desconto: {n - ((n*12)/100)}")
Pular_Linha()

#38
n = float(input("Salario: "))
print(f"Salario + aumennto: {((n*25)/100) + n}")
Pular_Linha()

#39
print("Premio de 780K pa 3 pessoa")
print(f"A 1° ficou com {(780*46/100)*1000 }")
print(f"A 2° ficou com {(780*32/100)*1000 }")
print(f"A 3° ficou com {(780*22/100)*1000 }")
Pular_Linha()

#40
n = int(input("Quantos dias vc vai trampar?: "))
formula = (30 - (30*8/100)) * n
print(f"Vc vai trampar {n} dias e vai ganhar {formula}")
Pular_Linha()

#41
n = int(input("Quantas horas vc trampa por dia?: "))
n1 = float(input("Quanto vc ganha por hora?: "))
formula = ((30 * n) * n1)
print(f"Vc vai ganhar no fim do mes {formula} + 10% vai ficar {formula + ((formula*10)/100)}")
Pular_Linha()

#42
n = float(input("Qual seu salario?: "))
formula = (n + (n*5)/100)
print(f"Seu salario base + 5% é {formula} menos o imposto de renda fica {(formula - (formula*7)/100)}")
Pular_Linha()

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
Pular_Linha()

#44
hd = float(input("Qual altura do degrau?: "))
h = float(input("Qual altura vc deseja alcançar?: "))
formula = round(h/hd)
print(f"Vc vai ter q subir {formula} degraus da escada")
Pular_Linha()

#45
n = input("Escreve 1 letra ai: ").upper()
print(f"Convertendo {n} pra {n.lower()}")
Pular_Linha()

#46
n = input("Escreve 1 numero INTEIRO ai: ")
#Transformo o número digitado em uma lista
n = list(n)
#Faço a orndenação inversa da lista, aqui eu já teria um resultado bem próximo
n.reverse()
print(n, type(n))
#Converto a lista para uma string e depois para inteiro
n = int("".join(n))
print(n)
Pular_Linha()

#47
n = input("Escreve 1 numero INTEIRO ai: ")
n = list(n)
print(n[0],"\n",n[1],"\n",n[2],"\n",n[3])
Pular_Linha()

#48
#Usei essa aula pra fazer esse daki
# https://youtu.be/wy11FiG_U9E
n = int(input("Digite segundos Inteiros ai: "))
h = n / 3600
m = (n % 3600) / 60
s = (n % 3600) % 60

print(f"{round(h)}H {round(m)}M {round(s)}S")
Pular_Linha()

#49
#Ja tava puto e me deu 1 preguiça da porra de fazer esse aki, ai peguei nesse site aki
# https://brainly.com.br/tarefa/38885954
print('Preencha os campos abaixo com o horário atual')

h = int(input('Hora: '))

m = int(input('Minuto: '))

s = int(input('Segundo: '))

d = int(input('\nDuração do evento (segundos): '))

s_final = (s + d) % 60

m_final = ( m + (s+d)//60 ) % 60

h_final = ( h + ( m + (s+d)//60 )//60 ) % 24

print(f'O fim do evento se dará às {h_final}h {m_final}min e {s_final} segundos')
Pular_Linha()

#50
n = int(input("Digita sua idade: "))
n = 2022 - n
print(f"Vc nasceu no ano de {n}")
Pular_Linha()

#51
#pitágoras
x = float(input("X: "))
y = float(input("Y: "))
# z² = x² + y²
z = (x*x) + (y*y)
z = z**0.5
print(f"Distancia é {z}")
Pular_Linha()

#52
print("Premio de 870K pa 3 amigos")
n1 = float(input("Quanto o 1° vai investir na loteria de 870K?:"))
n2 = float(input("Quanto o 2° vai investir na loteria de 870K?:"))
n3 = float(input("Quanto o 3° vai investir na loteria de 870K?:"))

t = n1+n2+n3
a1 = n1*100/t
a2 = n2*100/t
a3 = n3*100/t

print(f"O 1° ficou com {(870*a1/100)*1000 }")
print(f"O 2° ficou com {(870*a2/100)*1000 }")
print(f"O 3° ficou com {(870*a3/100)*1000 }")
Pular_Linha()

#53
c = float(input("Comprimento: "))
l = float(input("Largura: "))
p = float(input("Preço por metro de rede: "))

formula = c*l
formula = formula**2
formula = formula*p

print(f"Vai custar {formula} pra redear td terreno")