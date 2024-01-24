#53
#https://pt.stackoverflow.com/questions/467071/como-deixar-as-colunas-do-tri%C3%A2ngulo-de-floyd-perfeitamente-sim%C3%A9tricas
n = int(input(f'Digite o número de linhas: '))

m = 1
for c in range(1, n + 1):
    for i in range(1, c + 1):
        print(f'{m:<4}', end='')
        m += 1
    print()