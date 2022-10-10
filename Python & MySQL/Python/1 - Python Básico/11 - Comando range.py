# Comando range retorna uma lista

for i in range(10):
    print(i)
# Repare que vc pediu para fazer uma lista COM 10 numeros, + N foi mostrado o valor 10 PORRR QUUEEEE
# ela começa a contagem no valor 0, e do 0 ao 9 contem 10 numeros 

for i in range (15, 20): 
    print(i)
# Aki ele pegara do 1° elemento até o ultimo elemento -1, pois o ultimo numero é o valor de teto, ele não conta PPPORR QQQQUEEE
# ele quer de 15 a 20, de 15 a 20 tem 5 nuemros, 15,16,17,18,19, e 5 valores são o caminho até o valor final, ja tendo isso ele não mostra o valor final

for i in range(1, 16, 4):# passo de contagem
    print(i)
# Aki esta dando condição para percorrer, quero os valores de 1 até 16 indo de 4 em 4,
# Ele somara 4 a 1, e dps sucetivamente, repare que ele deu 13 e não 16, PQ, 13+4=17, ele não vai mostrar o valor que passar o valor de teto

for i in range(0,10,2):
    print(i) # e nem se chegar ao valor de teto ele vai mostrar

# POREM

for i in range(0,10 + 1,2): # ou (0,11,2)
    print(i) # so prescisa pegar 1 casa acima ou somar +1 ao valor de teto para ele mostrar
