#11
#Encontrei nesse site em C e adaptei pra python
#https://www.portugal-a-programar.pt/forums/topic/23208-programa-que-leia-um-n%C3%BAmero-inteiro-e-calcule-a-soma-dos-seus-d%C3%ADgitos/
#https://www.youtube.com/watch?v=5i5hmY6j7dM
''''''''''''''''''''''
numero = int(input("numero :  "))

somatorio=0

while (numero>0):

    resto = numero % 10
    numero = (numero-resto) / 10
    somatorio = somatorio + resto

print(f"O somatório é {somatorio}")
'''''''''''''''''''''''
#Também encontrei de outra forma mais simples usando MAP() e SUM()
#https://acervolima.com/programa-python-para-somar-os-digitos-de-um-determinado-numero/#:~:text=O%20m%C3%A9todo%20int()%20%C3%A9,dos%20d%C3%ADgitos%20em%20cada%20itera%C3%A7%C3%A3o.&text=M%C3%A9todo%202%3A%20Usando%20m%C3%A9todos%20sum,somar%20os%20n%C3%BAmeros%20na%20lista.
#tem q colocar o N como string pro map converter, acho que é isso, eu não entendi mt bem
''''''''''''''''''''''
n = str(input("Numero:  "))

list_of_number =map(int, n)

print(  (sum(list_of_number)) )
'''''''''''''''''''''
#isso aki ajudou
#https://www.geeksforgeeks.org/python-map-function/
#http://devfuria.com.br/python/built-in-list/
#Peguei a manha

n = int(input("Numero:  "))

if n > 0:
    #convertelo pra string e dps pra lista
    m = list(str(n))
    #pro map() fazer o mapeamento e converter em inteiro
    lista_numero =map(int, m)
    #dps sola-lo
    print(  (sum(lista_numero)) )

else:
    print("Numero invalido")