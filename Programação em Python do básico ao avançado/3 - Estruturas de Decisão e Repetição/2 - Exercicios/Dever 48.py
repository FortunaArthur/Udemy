#48
# https://franciscochaves.com.br/blog/fibonacci-em-python
anterior = 0
proximo = 0

n = int(input("Numero: "))

while(proximo < n):
    proximo = proximo + anterior
    anterior = proximo - anterior
    proximo += proximo

    if proximo > 4*(10**6):
        False
        break

print(proximo)