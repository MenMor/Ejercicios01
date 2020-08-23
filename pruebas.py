"""num = 34.87
entero = num // 1
decimal = num - entero
print(entero)
print(decimal)"""

"""diccionario_haxa = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

lista = [2, 10, 9, 15]

for i in range(0, len(lista)):
    if lista[i] == diccionario_haxa[10]:
        print(lista)"""


"""#binario a decimal
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
num = salida
vec = []
while num >= 1:
    vec.append(str(num % 8))
    num //= 8
print("octal es:", "".join(vec[::-1]))
# a hexadecimal es
num = salida
vec = []
diccionario_haxa = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
while num >= 1:
    vec.append(str(num % 16))
    num //= 16
print("hexadecimal es:", "".join(vec[::-1]))

for i in range(0, len(vec)):
    if vec[i] >= 10:
        if vec[i] == 10:
            vec.insert(i, "A")
        elif vec[i] == 11:
            vec.insert(i, "B")
        elif vec[i] == 12:
            vec.insert(i, "C")
        elif vec[i] == 13:
            vec.insert(i, "D")
        elif vec[i] == 14:
            vec.insert(i, "E")
        else:
            vec.insert(i, "F")

print("hexadecimal es:", "".join(vec[::-1]))"""

