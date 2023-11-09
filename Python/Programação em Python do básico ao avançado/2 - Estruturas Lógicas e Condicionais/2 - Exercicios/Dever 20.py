#20
#peguei daki, fikei cansado p krl, exercicio de corno essa questão
#https://www.pythonprogressivo.net/2018/02/Curso-Triangulo-Equilatero-Isosceles-Escaleno.html
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

# Testando se é triângulo
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')

#Triângulo Equilátero: três lados iguais;
elif (a == b) and (a == c) :
    print('Equilatero')

#Triângulo Isósceles: quaisquer dois lados iguais;
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')

#Triângulo Escaleno: três lados diferentes;
else:
    print('Escaleno')