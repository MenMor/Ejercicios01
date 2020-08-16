# Conversión de un entero con cualquier base a decimal

numero = int(input("Ingrese valor a convertir: "))
base = int(input("Ingrese base del valor: "))
num_output = numero

# Ingresar valores en lista de forma invertida
lista_numeros = []
bucle = 4
while bucle == 4:
    invertir = numero % 10
    lista_numeros.append(invertir)
    numero //= 10
    if numero == 0:
        bucle = 6  # bucle termina
print(lista_numeros)

sumatoria = 1  # Al estar elevado a potencia 0 siempre dara 1 primero posicion
exponente = 1
for i in range(1, len(lista_numeros)):
    producto = lista_numeros[i] * (base ** exponente)
    exponente += 1
    sumatoria += producto

print(f"Conversión de {num_output} a decimal = {sumatoria} con base 10 ")