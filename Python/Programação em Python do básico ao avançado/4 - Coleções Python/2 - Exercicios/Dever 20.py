#20
# ESTE AKI FOI 1 PUTA CODIGO DE CORNO QUE EU N FAZIA IDEIA DE COMO FAZER
# PEGUEI DAKI
# https://brainly.com.br/tarefa/37911702
def mostra_vetor (lst) :
    cont = 0
    while True:
        try :
            print(lst [cont], end=" ")

            cont += 1
            if cont%2 == 0:
                print( )
        except:
            break

Ist_int = list()
Ist_impares = list()
print(' Envie 10 numeros inteiros no intervalo fechado [0, 50]')

for i in range(10) :
    while True:
        try :
            num = int(input(f"Digite o {i+1} numero: "))

            if 0 <= num <= 50:
                Ist_int. append(num)
                break
            else:
                print('Entrada invalida! 0 numero deve estar no intervalo [0, 50]')
                continue
        except:
            print('Entrada invalida! Digite um numero inteiro no intervalo [0,50]')

for numero in Ist_int:
    if numero%2 != 0:
        Ist_impares . append(numero)

print('\nPrimeiro vetor: ' )
mostra_vetor (Ist_int)
print ("\nSegundo vetor vetor: ")
mostra_vetor(Ist_impares)