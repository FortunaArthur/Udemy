#17
l = []

for i in range(1,6):
    a = int(input("Valor: "))
    l.append(a)

print(l,"\n")

ind = [] # 1° descobrir os negativos
for i in l:
    if i < 0:
        ind.append(i)

indx = [] # descobrir os indices dos negativos
for i in ind:
    indx.append(l.index(i))

for i in indx: # resolver
    del(l[i])
    l.insert(i,0)
# ESSA PORRA LEVO TEMPO P KRL
print(l)