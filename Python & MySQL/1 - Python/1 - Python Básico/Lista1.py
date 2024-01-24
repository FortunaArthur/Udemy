#1
while True:
    try:
        i = int(input("Qual tua idade?: "))

        if i > 18:
            print("VC é maior de idade")
            False
            break

        else:
            print("VC é menor de idade")
            False
            break

    except ValueError:
        print("É NUMERO KRL")

#2
while True:

    try:

        nota1 = float(input('Primeira nota: '))
        nota2 = float(input('Segunda nota: '))

        media = (nota1 + nota2) / 2

        if media >= 6 :
            print('Media:',media, 'Aprovado')
            False
            break
            
        elif media < 6:
            print('Media:',media, 'Aprovado')
            False
            break

    except ValueError:
        print("É NUMERO PORRA")

#3
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
 
delta = ((b*b) - (4*a*c))
raiz_delta = delta ** 0.5
 
if delta < 0:
    print(delta, "=>Delta negativo")

else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", round(x1,2), "e", round(x2,2))

#4
lista = []

for i in range(0,3):
    a = int(input("Numero: "))
    lista.append(a)

print(sorted(lista))

#5
while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print("\n + => adição \n - => subtração \n * => multiplicação \n / => divisão \n")

        sinal = input("Digite o sinal: ")
        
        if sinal == "+":
            print(f"{n1} + {n2} = {n1+n2}")
            False
            break
        
        elif sinal == "-":
            print(f"{n1} - {n2} = {n1-n2}")
            False
            break

        elif sinal == "*":
            print(f"{n1} * {n2} = {n1*n2}")
            False
            break

        elif sinal == "/":
            print(f"{n1} / {n2} = {n1/n2}")
            False
            break
        
        else:
            print("Sinal inválido.")
    
    except ValueError:
        print("numero krl")