numero_uno = int(input("Ingrese primer numero binario: "))
numero_dos = int(input("Ingrese segundo numero binario: "))

vector_uno = []
vector_dos = []

i = 2
while i == 2:
    digito_uno = numero_uno % 10
    numero_uno //= 10
    vector_uno.append(digito_uno)
    if numero_uno == 0:
        i = 7

j = 2
while j == 2:
    digito_dos = numero_dos % 10
    numero_dos //= 10
    vector_dos.append(digito_dos)
    if numero_dos == 0:
        j = 7

"""entero = decimal // 1
dec = decimal - entero
print(entero)
print(dec)"""



"""# Convertir lista de cadena a entero
for j in range(0, len(cad_decimal)):
    parte_entera = (list(map(int, parte_entera)))
    parte_decimal = (list(map(int, parte_decimal)))
print(parte_entera)
print(parte_decimal)

# invierto lista entero
invertida_entero = []
for i in range(len(parte_entera)-1, -1, -1):
    invertida_entero.append(parte_entera[i])"""


