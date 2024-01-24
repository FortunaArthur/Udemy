#37
#Sem saco pra fazer essa tb, vsf grande da porra
#https://gist.github.com/AlyoshaS/93d231d3e54c2af1d4c10f351b1a2cd2
#1° Versão
hora_chegada, min_chegada = [int(x) for x in input("Digite a hora e minuto de chegada (** **  e ** **): ").split()]
hora_partida, min_partida = [int(x) for x in input("Digite a hora e minuto de saída (** **  e ** **): ").split()]

# Define horario:
if hora_chegada > hora_partida:
    hora_partida = hora_partida + 24
if min_chegada > min_partida:
    min_partida = min_partida + 60
    hora_partida = hora_partida - 1

min_final = min_partida - min_chegada
hora_final = hora_partida - hora_chegada

if hora_final >= 1:
    if min_final > 1:
        print("O carro ficou estacionado durante %d horas e %d minutos." % (hora_final, min_final))
    else:
        print("O carro ficou estacionado durante %d horas." % (hora_final))
else:
    print("O carro ficou estacionado durante %d minutos." % (min_final))

# Define valores:
min_total = int((hora_final * 60) + min_final)

if min_total <= 120:
    if min_total <= 60:
        preco = 1.00
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2
        print("Preço total: R$%.2f." % (preco))
elif min_total <= 240:
    if min_total <= 180:
        preco = 2 + 1.40
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2 + (1.40 * 2)
        print("Preço total: R$%.2f." % (preco))
else:
    hora_total = int(min_total // 60)
    preco = 4.40 + ((hora_total - 4) * 2)
    print("Preço total: R$%.2f." % (preco))

#2° Versão
h_entrada = int(input("Digite a hora de entrada \n"))
m_entrada = int(input("Digite os minutos de entrada \n"))
h_saida = int(input("Digite a hora de saída \n"))
m_saida = int(input("Digite os minutos de saída \n"))

# cálculo da permanência

if h_entrada > h_saida:
    hora_final = (h_saida + 24) - h_entrada
else:
    hora_final = h_saida - h_entrada

if m_entrada > m_saida:
    minuto_final = (m_saida + 60) - m_entrada
else:
    minuto_final = m_saida - m_entrada

print(f"A permanência foi de: {hora_final} horas e {minuto_final} minutos \n")

# cálculo do valor

tempo_minutos = hora_final * 60 + minuto_final

if 1 <= tempo_minutos <= 60:
    preco = 1
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 60 < tempo_minutos <= 120:
    preco = 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 120 < tempo_minutos <= 180:
    preco = 4.2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 180 < tempo_minutos <= 240:
    preco = 5.6
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif tempo_minutos > 240:
    preco = hora_final * 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
else:
    print(f"Tempo de permanência mínimo, não será necessário pagar!")