
print("Binario a decimal, octal y hexadecimal.")

binario = int(input("Ingrese valor binario: "))
out_binario = binario

# Ingresar valores en lista de forma invertida
lista_numeros = []
bucle = 4
while bucle == 4:
    invertir = binario % 10
    lista_numeros.append(invertir)
    binario //= 10
    if binario == 0:
        bucle = 6  # bucle termina

# Binario a decimal
decimal = 0
for i in range(0, len(lista_numeros)):
    decimal += lista_numeros[i] * (2**i)

print(f"{decimal} base 10")

# A octal
octal_conversion = decimal
a = 1
octal = 0
i = 2
while i == 2:
    valor = octal_conversion % 8
    octal += valor * a
    a *= 10
    octal_conversion //= 8
    if octal_conversion == 0:
        i = 3
print(f"{octal} base 8")

# A hexadecimal
hexadecimal_conv = decimal
list_hexadecimal = []
i = 2
while i == 2:
    residuo = hexadecimal_conv % 16
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
    hexadecimal_conv //= 16
    if hexadecimal_conv == 0:
        i = 3

valor_hexadecimal = []
for j in range(len(list_hexadecimal)-1, -1, -1):
    valor_hexadecimal.append(list_hexadecimal[j])

print(f"{valor_hexadecimal} base 16")


