numero = int(input("Ingrese numero decimal: "))
numero_original = numero
list_hexadecimal = []
i = 2
while i == 2:
    residuo = numero % 16
    if residuo >= 10:
        if residuo == 10:
            list_hexadecimal.append("A")
        elif residuo == 11:
            list_hexadecimal.append("B")
        elif residuo == 12:
            list_hexadecimal.append("C")
        elif residuo == 13:
            list_hexadecimal.append("D")
        elif residuo == 14:
            list_hexadecimal.append("E")
        else:
            list_hexadecimal.append("F")
    else:
        list_hexadecimal.append(residuo)
    numero //= 16
    if numero == 0:
        i = 3

list_invertida = []
for j in range(len(list_hexadecimal)-1, -1, -1):
    list_invertida.append(list_hexadecimal[j])

print(f"{numero_original} decimal a hexadecimal = {list_invertida} base 16")
