#38
# irmão GPT fez p mim, se fude essa questão
def insere_ordenado(vetor, valor):
    # Insere o valor no vetor mantendo a ordem crescente
    i = len(vetor) - 1
    while i >= 0 and vetor[i] > valor:
        vetor[i + 1] = vetor[i]
        i -= 1
    vetor[i + 1] = valor

# Cria um vetor vazio para armazenar os valores ordenados
vetor_ordenado = []

# Solicita ao usuário que digite dez valores
for _ in range(10):
    valor = float(input("Digite um valor numérico: "))

    # Insere o valor no vetor mantendo a ordem crescente
    insere_ordenado(vetor_ordenado, valor)

# Exibe o vetor ordenado
print("Valores em ordem crescente:", vetor_ordenado)
