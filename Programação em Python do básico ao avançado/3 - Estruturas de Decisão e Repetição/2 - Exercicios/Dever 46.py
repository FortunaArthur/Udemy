#46
import random
a = random.randint(1,1000)

while True:
    n = int(input("Numero: "))

    if n > a:
        print("Valor mais alto que A, ABAIXA")
    elif n < a:
        print("Valor mais baixo que A, AUMENTA")
    else:
        print("Acerto")
        False
        break