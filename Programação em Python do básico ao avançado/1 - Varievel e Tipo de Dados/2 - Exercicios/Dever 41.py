#41
n = int(input("Quantas horas vc trampa por dia?: "))
n1 = float(input("Quanto vc ganha por hora?: "))
formula = ((30 * n) * n1)
print(f"Vc vai ganhar no fim do mes {formula} + 10% vai ficar {formula + ((formula*10)/100)}")