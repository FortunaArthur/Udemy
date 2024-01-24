#35
# irmão GPT fez p mim, se fude essa questão
def cria_vetor(numero):
    # Converte o número para uma lista de dígitos
    return [int(digito) for digito in str(numero)]

def soma_vetores(vetor_a, vetor_b):
    resultado = []
    carry = 0  # Variável para armazenar o "vai um" das somas

    # Garante que ambos os vetores têm o mesmo comprimento
    len_a, len_b = len(vetor_a), len(vetor_b)
    if len_a < len_b:
        vetor_a += [0] * (len_b - len_a)
    elif len_b < len_a:
        vetor_b += [0] * (len_a - len_b)

    # Realiza a soma dos vetores
    for digito_a, digito_b in zip(vetor_a, vetor_b):
        soma = digito_a + digito_b + carry
        carry = soma // 10  # Determina se há um "vai um"
        resultado.append(soma % 10)

    # Se houver carry no final, adiciona ao resultado
    if carry:
        resultado.append(carry)

    return resultado

# Obtém os números de entrada
a = int(input("Digite o primeiro número (positivo, menor que 10000): "))
b = int(input("Digite o segundo número (positivo, menor que 10000): "))

# Cria os vetores
vetor_a = cria_vetor(a)
vetor_b = cria_vetor(b)

# Realiza a soma dos vetores
resultado = soma_vetores(vetor_a, vetor_b)

# Exibe os resultados
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Soma: {resultado}")
