#25
soma3 = 0
soma5 = 0
for i in range (1000):
   if i % 3 == 0:
       soma3 += i

   elif i % 5 == 0:
       soma5 += i

print(f"soma dos multiplos de 3: {soma3}")
print(f"soma dos multiplos de 5: {soma5}")
print(f"soma total: {soma3 + soma5}")