#37
# irmão GPT fez p mim, se fude essa questão
def merge(vetor, inicio, meio, fim):
    # Função auxiliar para mesclar duas partes ordenadas do vetor
    parte_esquerda = vetor[inicio:meio+1]
    parte_direita = vetor[meio+1:fim+1]

    i = j = 0
    k = inicio

    # Mescla as partes ordenadas
    while i < len(parte_esquerda) and j < len(parte_direita):
        if parte_esquerda[i] <= parte_direita[j]:
            vetor[k] = parte_esquerda[i]
            i += 1
        else:
            vetor[k] = parte_direita[j]
            j += 1
        k += 1

    # Adiciona os elementos restantes, se houver
    while i < len(parte_esquerda):
        vetor[k] = parte_esquerda[i]
        i += 1
        k += 1

    while j < len(parte_direita):
        vetor[k] = parte_direita[j]
        j += 1
        k += 1

def merge_sort(vetor, inicio, fim):
    # Algoritmo Merge Sort para ordenar o vetor
    if inicio < fim:
        meio = (inicio + fim) // 2

        # Ordena as duas metades
        merge_sort(vetor, inicio, meio)
        merge_sort(vetor, meio+1, fim)

        # Mescla as partes ordenadas
        merge(vetor, inicio, meio, fim)

# Exemplo de uso:
vetor = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7, 6]
merge_sort(vetor, 0, len(vetor)-1)
print("Vetor ordenado:", vetor)
