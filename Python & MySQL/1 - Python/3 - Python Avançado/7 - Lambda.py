# se teria q fazer uma função pra algo q fosse ultilizado 1 vez, então é só usar o lambda
valor = [1,2,3,4,5]
# função lambda vai receber e criar uma função e será executada numa unica linha
# pra kd valor será interpretado como a variavel "i" , e nessa função ela quer armazenar o dobro, assim "i*2"
dobrado = list(map(lambda i: i*2, valor))
# o obejtivo da funçao lambda é criar umafunção que será executada uma unica vez, e assim economiza espaço
# o lambda geralmente vem combinado de outras funções, nesse caso o map
print(dobrado)