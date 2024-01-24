#9
n1 = float(input("Digite seu salario: "))
n2 = float(input("Digite a prestação do emprestimo: "))

p = (n2 * 100) / n1

if p > 20:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")