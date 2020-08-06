# Realizar un algoritmo que calcule el valor aproximado de pi, basado en el método de Euler

print("Aproximación pi por el método de Euler")
limite = int(input("Ingrese límite para aproximación: "))

if limite == 0:
    print("Pi = 1")

sumatoria = 1
for n in range(1, limite + 1):
    factorial_pi = 1
    for i in range(2, n + 1):  # cálculo del factorial
        factorial_pi *= i

    D = 2 * n + 1  # cálculo del paréntesis del denominador
    denominador_factorial = 1
    for j in range(1, D+1):  # cálculo del denominador del factorial
        denominador_factorial *= j

    sumatoria += (2**n * factorial_pi**2) / denominador_factorial

print(f"pi/2 = {sumatoria} \nAproximación de pi = {sumatoria * 2}")





# Encontrar el promedio de todos los números primos que hay entre 1 y n, donde n es el límite del rango.

print("\nValor aproximado de pi, basado en el producto de Wallis")

limite = int(input("Introduzca límite: "))

pi = 1
n = 1
while n <= limite:
    formula = ((2 * n) / (2 * n - 1)) * ((2 * n) / (2 * n + 1))
    pi *= formula
    n += 1
print(f"Pi/2 = {pi} \nAproximación de pi = {pi * 2}")

# Con for
print("\nValor aproximado de pi, basado en el producto de Wallis")

lim = int(input("Introduzca límite: "))
acum = 1
for n in range(1, lim+1):
    form = ((2 * n) / (2 * n - 1)) * ((2 * n) / (2 * n + 1))
    acum *= form
print(f"Pi/2 = {acum} \nAproximación de pi = {acum * 2}")





# Realizar un programa que calcule el dígito verificador de la cédula ecuatoriana. Con listas.

print("\nDígito verificador de la cédula ecuatoriana.")

cedula = []
for i in range(0, 9):
    digito_in = int(input(f"Ingrese {i+1} dígito de cédula: "))
    cedula.insert(i, digito_in)  # Inserto en la posición: i y el valor de entrada a lista
print(cedula)

suma_impares = 0
for j in range(0, 9, 2):
    cedula[j] = cedula[j] * 2
    if cedula[j] > 9:
        cedula[j] -= 9
    suma_impares += cedula[j]

suma_pares = cedula[1]+cedula[3]+cedula[5]+cedula[7]
suma_total = suma_pares + suma_impares

suma_total %= 10
if suma_total != 0:
    suma_total = 10 - suma_total
    print(f"Dígito verificador es: {suma_total}")
else:
    print(f"Dígito verificandor es : {suma_total}")





# Algoritmo que calcule el número de dígitos que tiene un número
print("\nCantidad de dígitos que tiene un número.")
numero = int(input("Ingrese número: "))
contador_u = 0
acumulador = 0
while numero > 0:
    ultimo_digito = numero % 10  # Quito último dígito
    contador_u += 1
    acumulador += ultimo_digito  # Guardo último dígito
    numero //= 10

print(f"Tiene: {contador_u} dígitos")





# Algoritmo que determine si un número es CAPICÚA, es decir, si al leerlo al revés es igual
print("\nValidación de número capicúa")

numero_capicua = int(input("Ingrese un número para validar si es capicúa: "))
num_capicua_2 = numero_capicua  # guardo valor

i = 2
a = 1
suma_1 = 0
while i == 2:  # bucle infinito
    ultimo_dig_1 = numero_capicua % 10  # guardo último digito
    numero_capicua //= 10  # quito último dígito
    multiplicacion = ultimo_dig_1 * a
    a *= 10
    suma_1 += multiplicacion
    if numero_capicua == 0:  # Finalizó bucle
        i = 3

b = a  # Asignó el último valor para comparar de atrás hacia adelante. Esto es porque no se cuantos digitos tiene
j = 2
suma_2 = 0
while j == 2:
    ultimo_dig_2 = num_capicua_2 % 10
    num_capicua_2 //= 10
    b /= 10  # Decremento valores que tenía en primer while.
    multiplicacion_2 = ultimo_dig_2 * b
    suma_2 += multiplicacion_2
    if num_capicua_2 == 0: # Término bucle
        j = 3

if suma_1 == suma_2:
    print("El número es capicua.")
else:
    print("Número no capicua.")



"""Dada una medida de tiempo expresada en horas, minutos y segundos con valores aleatorios.
   Elabore un programa que transforme dicha medida en una expresión correcta. Con bucles."""

print("\nMedida de tiempo.")

horas = int(input("Introduce horas:"))
min = int(input(" Introduce minutos"))
segundos = int(input("Introduce segundos"))

cont = 0
cont2 = 0
while segundos > 60:
     segundos -= 60
     cont += 1
min += cont
while min > 60:
     min -= 60
     cont2 += 1
horas += cont2
dias = horas//24
while horas > 24:
     horas -= 24

print(f"{dias} días {horas} horas {min} minutos {segundos} segundos ")




# Promedio números primos entre 1 a n. n es el límite del rango

print("\nPromedio números primos entre 1 a n. n es el límite del rango")

limite = int(input("Ingrese límite: "))

suma_promedio = 1
contador_primo = 1

for i in range(1, limite+1):
    cont = 0
    for j in range(1, limite+1):  # Bucle para verificar si i es divisible para un rango de j
        if i % j == 0:
            cont += 1
    if cont == 2:  # Solo será primo si es divisible para dos números.
        print(i)  # Imprimo todos los números primos
        suma_promedio += i
        contador_primo += 1

promedio = suma_promedio / contador_primo
promedio = round(promedio, 2)
print(f"Promedio números primos es: {promedio}")





# Calcular división de dos números a y b usando sólo sumas y restas


print("\nDivisión entera: ")
dividendo = int(input("Ingrese dividendo: "))
divisor = int(input("Ingrese divisor: "))

if divisor == 0:
    print("Error! división entre cero.")

elif dividendo > divisor:
    respuesta = 0
    x = 2
    while x != 1:
        dividendo -= divisor
        respuesta += 1
        if dividendo < divisor:
            print(f"División entera = {respuesta} Residuo = {dividendo}")
            x = 1  # fin bucle infinito

else:
    print("División entera = 0")  # Si dividendo < divisor





# Obtener número e (número de Euler)
print("\nNúmero de Euler")

limite = int(input("Ingresar límite para aproximación de número e: "))

sumatoria = 2  # 1/0! = 1 + 1/1! = 1 -> 2
formula = 1
i = 2  # Omito 2 pasos que dan 2 y los asigne a sumatoria
while i <= limite:
    factorial = 1
    for j in range(2, i+1):  # Factorial denominador
        factorial *= j

    formula = 1/factorial
    sumatoria += formula
    i += 1

print(f"e = {sumatoria}")





# Cálculo potencia de base y exponente, sólo con sumas.
print("\nPotencia")

base = int(input("Ingrese base: "))
exponente = int(input("Ingrese exponente: "))
acumulador_p = 0

if (exponente == 0) or (base == 0):
    print("Respuesta = 1")

elif base == 0:
    print("Respuesta = 0")

else:
    auxiliar = 1
    for i in range(1, exponente+1):
        acumulador_p = 0
        for j in range(1, base+1):
            acumulador_p += auxiliar
        auxiliar = acumulador_p

print(f"{base} ^ {exponente} = {acumulador_p}")