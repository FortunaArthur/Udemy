#51
funcionario = 2000
ano = 1995

while ano < 2022:
    ano += 1
    aumento = (1.5*funcionario)/100
    funcionario += aumento

    if ano == 1997:
        while True:
            ano += 1
            funcionario += (2*aumento)


            if ano == 2022:
                False
                break

print(ano, funcionario)