# Esse tratamento evita que o erro pare seu programa no meio da execução
a = 4
b = 0

print(a/b) #é obvio q isso aki vai dar erro, n tem como fazer divisão por 0, e esse erro vai travar o programa ENTÃOOO..

try:# TENTE FAZER ISSO

    print(a/b) # SERA FEITO ISSO, CASO TENHA 1 ERRO, NO CASO ELE NÃO CONSIGA FAZER ISSO, AI ELE ETRA NO EXCEPT

except:# SE NÃO FASSA ISSO (EXEÇÃO)
    print("NÃO pode dividir por 0")