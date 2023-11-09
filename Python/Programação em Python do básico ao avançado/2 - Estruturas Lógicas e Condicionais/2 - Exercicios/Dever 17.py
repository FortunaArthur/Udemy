#17
BM = float(input("Base Maior: "))
bm = float(input("Base Menor: "))
h = float(input("Altura: "))

a = ((BM + bm) * h)/2

if (BM > 0) & (bm > 0) & (h > 0):
    print(f"Área do Trapézio: {a}")
else:
    print("Valores errados")