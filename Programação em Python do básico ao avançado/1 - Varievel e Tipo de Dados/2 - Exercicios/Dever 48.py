#48
#Usei essa aula pra fazer esse daki
# https://youtu.be/wy11FiG_U9E
n = int(input("Digite segundos Inteiros ai: "))
h = n / 3600
m = (n % 3600) / 60
s = (n % 3600) % 60

print(f"{round(h)}H {round(m)}M {round(s)}S")