#29
import math
l1 = []
for i in range(1, 11):
    l1.append(i)

#o corno quer só para 5 termos então vai ser isso msm
S = 0 + (1/ math.prod(l1[1::-1])) + (2/ math.prod(l1[3::-1])) + (3/ math.prod(l1[5::-1])) + (4/ math.prod(l1[7::-1])) + (5/ math.prod(l1[9::-1]))

print(S)