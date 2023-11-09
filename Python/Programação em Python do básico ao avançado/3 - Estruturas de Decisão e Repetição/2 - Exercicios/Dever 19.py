#19
while True:
    a = (int(input('insira um numero entre 100 e 999: ')))

    if a > 100 and a < 999:
       break

    else:
        a
# http://devfuria.com.br/python/built-in-enumerate/
#Tem q transformar pra string pra o enumerate percorrer
b = str(a)
for i, v in enumerate(b):
    # o V é os valores e o I éa  posição
   print(v)