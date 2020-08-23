import numpy as np

lim = int(input("Ingrese limite: "))
suma = 0
leibniz = np.arange(0, lim)
suma += np.sum(((-1)**leibniz) / (2*leibniz+1))
print(f"pi = {suma*4}")


suma_pi = 0
pi = np.arange(0, 1000)
suma_pi += np.sum(((-1)**pi) / (2*pi+1))
print(f"pi = {suma_pi*4}")

