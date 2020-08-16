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

for i in range(0, len(vector_uno)):
    for j in range(0, len(vector_dos)):
        suma += vector_uno


