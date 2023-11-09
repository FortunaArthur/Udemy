#41
t = True

while t :
    r1 = int(input("R1:"))
    r2 = int(input("R2:"))

    R = (r1*r2) / (r1+r2)

    if (r1 & r2) == 0 or R == 0:
        print("R = 0")
        t = False

    else:
        print(R)