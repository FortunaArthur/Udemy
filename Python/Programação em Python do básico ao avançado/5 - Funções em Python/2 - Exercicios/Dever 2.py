#2
def data_por_extenso(data):
    # Mapeamento dos meses
    meses = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }

    # Separa a data em dia, mês e ano
    dia, mes, ano = map(int, data.split('/'))

    # Formata a data por extenso
    data_extenso = f"{dia} de {meses[mes]} de {ano}"

    return data_extenso

# Testa a função
print(data_por_extenso(input("Data: ")))
