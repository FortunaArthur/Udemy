#33
n = int(input("Numero: "))
i = int(input("Numero I: "))
j = int(input("Numero J: "))

for x in range (0, n+1):

   if (x % i == 0) or  (x % j == 0):
       print(x, end=",")