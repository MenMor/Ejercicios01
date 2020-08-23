import numpy as np
entrada = input("ingrese el número binario: ")
cadena = entrada[::1]
salida = 0; expo = 0
while expo < len(cadena):
    if (int(cadena[expo]) == 1):
        salida += int(cadena[expo]) * 2 ** expo
    expo += 1
print(" el resultado es: ", salida)
# a es octal
num= salida
vec = []
while num >= 1:
    vec.append(str(num % 8))
    num //= 8
print("octal es:", "".join(vec[::-1]))
# a hexadecimal es
num= salida
vec = []
while num >= 1:
    vec.append(str(num % 16))
    num //= 16
print("hexadecimal es:", "".join(vec[::-1]))