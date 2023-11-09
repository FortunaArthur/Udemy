#49
carlos = float(input("Qual teu salario: "))
joao = carlos/3

meses = 0

while True:
    p_carlos = (2*carlos)/100
    p_joao = (5*joao)/100
    meses += 1
    carlos += p_carlos
    joao += p_joao

    if joao > carlos:
        print(meses," Meses")
        False
        break