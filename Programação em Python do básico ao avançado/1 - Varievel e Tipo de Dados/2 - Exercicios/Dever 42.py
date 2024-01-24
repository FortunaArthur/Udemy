#42
n = float(input("Qual seu salario?: "))
formula = (n + (n*5)/100)
print(f"Seu salario base + 5% é {formula} menos o imposto de renda fica {(formula - (formula*7)/100)}")