#33
#https://stackoverflow.com/questions/49973739/python-how-to-remove-zeroes-from-a-list-in-python
l = []
for i in range(0,15):
    a = int(input("N: "))
    l.append(a)

X = [i for i in l if i != 0]
print(X)