"""Convertir un número en base 10 con decimal, almacenado en una variable float,
   a su correspondiente en base Binaria, octal y hexadecimal, todas estas almacenadas en vectores."""

decimal = float(input("Ingrese decimal: "))

# Separo parte entera y parte decimal
cad_decimal = str(decimal)

parte_entera = []
parte_decimal = []

posicion_punto = 0
for i in range(0, len(cad_decimal)):
    if cad_decimal[i] == '.':
        posicion_punto = i
        parte_entera = (cad_decimal[0: posicion_punto])
        parte_decimal = (cad_decimal[posicion_punto+1:])


# Convierto en números enteros
entero_num = int(parte_entera[:])
int_octal = entero_num
int_hexa = entero_num

decimal_num = int(parte_decimal[:])
# lo vuelvo punto decimal 0.?
long = str(decimal_num)
longitud = len(long)
i = 0
x = 1
while i <= longitud-1:
    x *= 10
    i += 1
decimal_num /= x
dec_octal = decimal_num
dec_hexa = decimal_num



# Decimal a binario
# Calcúlo parte entera de decimal a binario
binario_entero = []
i = 1
while i == 1:
    residuo = entero_num % 2
    binario_entero.append(residuo)
    entero_num //= 2
    if entero_num == 0:
        i = 3
invertida_entero = []
for i in range(len(binario_entero)-1, -1, -1):
    invertida_entero.append(binario_entero[i])

# calcúlo parte decimal a binario
binario_decimal = [".", ]
i = 2
while i == 2:
    decimal_num *= 2
    resultado = decimal_num // 1
    resultado = round(resultado)
    binario_decimal.append(resultado)
    if decimal_num == 1:
        i = 5

#Hago una sola lista de resultado
for i in range(0, len(binario_decimal)):
    invertida_entero.append(binario_decimal[i])

print(f"De decimal {decimal} a binario = {invertida_entero} base 2.")



# Decimal a octal:

entero_octal = []
i = 3
while i == 3:
    residuo_octal = int_octal % 8
    entero_octal.append(residuo_octal)
    int_octal //= 8
    if int_octal == 0:
        i = 7
invertida_octal_int = []
for i in range(len(entero_octal)-1, -1, -1):
    invertida_octal_int.append(entero_octal[i])

octal_decimal = [".", ]
dec_octal *= 8
resultado_octal = dec_octal // 1
resultado_octal = round(resultado_octal)
octal_decimal.append(resultado_octal)

#Hago una sola lista de resultado
for i in range(0, len(octal_decimal)):
    invertida_octal_int.append(octal_decimal[i])

print(f"De decimal {decimal} a octal = {invertida_octal_int} base 8.")




# Decimal a Hexadecimal
# diccionario_haxa = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
entero_hexa = []
i = 6
while i == 6:
    residuo_hexa = int_hexa % 16
    if residuo_hexa >= 10:
        if residuo_hexa == 10:
            entero_hexa.append("A")
        elif residuo_hexa == 11:
            entero_hexa.append("B")
        elif residuo_hexa == 12:
            entero_hexa.append("C")
        elif residuo_hexa == 13:
            entero_hexa.append("D")
        elif residuo_hexa == 14:
            entero_hexa.append("E")
        else:
            entero_hexa.append("F")
    else:
        entero_hexa.append(residuo_hexa)
    int_hexa //= 16
    if int_hexa == 0:
        i = 11

invertida_hexa_int = []
for i in range(len(entero_hexa)-1, -1, -1):
    invertida_hexa_int.append(entero_hexa[i])

hexa_decimal = [".", ]
dec_hexa *= 16
resultado_hex = dec_hexa // 1
resultado_hex = round(resultado_hex)
hexa_decimal.append(resultado_hex)


#Hago una sola lista de resultado
for i in range(0, len(hexa_decimal)):
    invertida_hexa_int.append(hexa_decimal[i])

print(f"De decimal {decimal} a hexadecimal = {invertida_hexa_int} base 16.")
