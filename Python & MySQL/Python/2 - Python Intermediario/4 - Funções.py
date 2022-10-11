# Blocos de codigo que vão funcionar quando chamados
def soma (x,y):
    print("x: ",x)
    print("Y: ",y)
    print(x + y)

soma(2,6)

#Outra Forma
def SOMA(X,Y):
    return X+Y

S = SOMA(3,7)
print(S)

#chamar
def multiplica(x,y):
    return y *x

m = multiplica(3,9)

print(soma(S,m))