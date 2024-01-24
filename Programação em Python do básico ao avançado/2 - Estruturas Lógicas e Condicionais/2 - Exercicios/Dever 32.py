#32
print("Cardapio | Codigo | Preço" + "\n"
"Dogão | 100 | 1.20"  + "\n"
"Bauru simples | 101 | 1.30"  + "\n"
"Bauru com ovo | 102 | 1.50"  + "\n"
"Hamburgão | 103 | 1.20"  + "\n"
"Hamburgão com queijo | 104 | 1.70"  + "\n"
"Sukinho | 105 | 2.20"  + "\n"
"Refri | 106 | 1.00"  + "\n")

cod = int(input("Qual o codigo: "))

if cod == 100:
    print("Vc vai pagar 1.20 pelo hotdog")
else:
    if cod == 101:
        print("Vc vai pagar 1.30 pelo Bauru simples")
    else:
        if cod == 102:
            print("Vc vai pagar 1.50 pelo Bauru com ovo")
        else:
            if cod == 103:
                print("Vc vai pagar 1.20 pelo Hamburgão")
            else:
                if cod == 104:
                    print("Vc vai pagar 1.70 pelo Hamburgão com queijo")
                else:
                    if cod == 105:
                        print("Vc vai pagar 2.20 pelo Sukinho")
                    else:
                        if cod == 106:
                            print("Vc vai pagar 1.00 pelo Refri")