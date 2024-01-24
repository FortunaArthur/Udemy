#52
# https://www.clubedohardware.com.br/forums/topic/1395636-python-algoritmo-de-caixa-eletr%C3%B4nico/
saque = int(input('Digite o valor do saque: '))
total = saque #Montante total que será decomposto
nota = 100 #Tirar 100 reais do montante
totalnotas = 0
while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print('Total de {} notas de R$ {}' .format(totalnotas, nota))
        if nota == 100:
            nota = 50
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        totalnotas = 0
        if total == 0:
            break