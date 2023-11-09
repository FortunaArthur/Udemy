#12
#http://www.w3big.com/pt/python/func-number-log.html
from ast import Not
import math
from re import A, X
from tkinter.tix import InputOnly
n = int(input("Numero:  "))

if n > 0:
    print(f"Logaritimo de {n} é {math.log(n)}")
else:
    print("Numero invalido")