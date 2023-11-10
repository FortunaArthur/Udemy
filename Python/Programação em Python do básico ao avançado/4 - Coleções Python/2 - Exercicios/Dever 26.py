#26
# https://www.delftstack.com/pt/howto/python/standard-deviation-of-a-list-in-python/
# https://acervolima.com/calcule-a-media-variancia-e-desvio-padrao-em-python-usando-numpy/#:~:text=Desvio%20padr%C3%A3o%20em%20Python%20usando%20Numpy%3A%20Pode-se%20calcular,padr%C3%A3o%20usando%20a%20fun%C3%A7%C3%A3o%20numpy.std%20%28%29%20em%20python.
import numpy as np

list = [*range(1,11)]
print("List : " + str(list))

st_dev = np.std(list)

print("Standard deviation of the given list: " + str(st_dev))