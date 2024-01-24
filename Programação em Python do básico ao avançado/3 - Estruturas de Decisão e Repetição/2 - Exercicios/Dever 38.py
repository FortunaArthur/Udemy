#38
#Peguei desse site aki
#https://rafaeljsouza.medium.com/100-dias-de-c%C3%B3digo-dia-8-projeto-euler-9-ea31c530a985
A = 0
B = 0
C = 0
#0 até mil
for c in range (0,1000):
    # de 0 até mill MENOS o valor q c escolheu
    for b in range(0, 1000-c):
        #de 0 até 1 valor abaixo de b
        for a in range(0, b):
            if a + b + c ==1000 and a**2 + b**2 == c**2:
                A += a
                B += b
                C += c

print(A, B, C)