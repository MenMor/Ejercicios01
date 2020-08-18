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

sumatoria = 0
exponente = 0
for i in range(0, len(lista_numeros)):
    producto = lista_numeros[i] * (base ** exponente)  # cuando el exponente sea 0 siempre valdra 1. Regla exponete.
    exponente += 1
    sumatoria += producto

print(f"Conversión de {num_output} a decimal = {sumatoria} con base 10 ")
