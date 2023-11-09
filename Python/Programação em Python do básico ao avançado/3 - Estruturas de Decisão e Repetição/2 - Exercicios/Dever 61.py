#61
# https://pt.stackoverflow.com/questions/226102/encontrar-o-maior-pal%C3%ADndromo-feito-a-partir-do-produto-de-dois-n%C3%BAmeros-de-3-d%C3%ADgi
i = 0
j = 0
pol = 0
while i <= 999:
    j = i
    while j <= 999:
        temp = str(i * j)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            polTemp = int(temp)
            if polTemp > pol:
                pol = polTemp
        j += 1
    i += 1
print(pol)