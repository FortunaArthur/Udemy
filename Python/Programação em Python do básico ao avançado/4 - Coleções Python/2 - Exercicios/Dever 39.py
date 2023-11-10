#39
# https://www.delftstack.com/es/howto/python/python-pascal-triangle/#:~:text=Para%20formar%20un%20tri%C3%A1ngulo%20pascal%20en%20Python%2C%20hay,lista%20vac%C3%ADa%2C%20que%20se%20utiliza%20para%20almacenar%20valores.
num = int(input("Enter the number of rows:"))
for n in range(num):
    print(''*(num-n), end='')

    print(''.join(map(str, str(11**n))))
#VAI SE FUDER ESSE DEVER
