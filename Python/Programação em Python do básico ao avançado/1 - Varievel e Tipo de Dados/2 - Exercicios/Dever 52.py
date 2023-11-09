#52
print("Premio de 870K pa 3 amigos")
n1 = float(input("Quanto o 1° vai investir na loteria de 870K?:"))
n2 = float(input("Quanto o 2° vai investir na loteria de 870K?:"))
n3 = float(input("Quanto o 3° vai investir na loteria de 870K?:"))

t = n1+n2+n3
a1 = n1*100/t
a2 = n2*100/t
a3 = n3*100/t

print(f"O 1° ficou com {(870*a1/100)*1000 }")
print(f"O 2° ficou com {(870*a2/100)*1000 }")
print(f"O 3° ficou com {(870*a3/100)*1000 }")