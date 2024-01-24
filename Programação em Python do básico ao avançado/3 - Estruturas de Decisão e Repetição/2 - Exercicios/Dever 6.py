#6
s = 0 #  SOMA
q = 0 # N° DE VEZES DIGITADOS
for i in range (1,11):
  a = int(input("Numero: "))
  s = s + a # SOMA DOS INPUTS
  q = q + 1 # SOMA DAS VEZES
# : . 2f é pra colocar só 2 casas decimais
print(f"Média: {s/q:.2f}")