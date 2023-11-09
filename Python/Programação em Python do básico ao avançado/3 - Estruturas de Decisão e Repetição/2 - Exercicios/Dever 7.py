#7
#FOR
s = 0 #  SOMA
q = 0 # N° DE VEZES DIGITADOS
for i in range (1,11):
  a = int(input("Numero: "))
  if a > 0:
    s = s + a # SOMA DOS INPUTS
    q = q + 1 # SOMA DAS VEZES

  else:
    print("Não conta")

# : . 2f é pra colocar só 2 casas decimais
print("Soma: ", s)
print(f"Média: {s/q:.2f}")

#WHILE
soma = 0
quantidade = 0
while True:

  n = int(input("Digite um número inteiro: "))

  if n > 0:
    soma = soma + n
  else:
    print("Não conta")

  quantidade = quantidade + 1

  if quantidade == 10:
    break

print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")