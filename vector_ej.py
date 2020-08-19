import numpy as np

vector_1 = np.array([1, 2, 3, 4, 5, 6])  # Crear vector
print(vector_1[1:len(vector_1)-1])

vector_2 = np.array([i**2 for i in range(10) if i ** 2 % 2 == 0])
print(vector_2)

vector_pares = np.array([2*i for i in range(5*5)])
print(vector_pares)

vector_impar = np.array([i for i in range(0, 10, 3)])
print(vector_impar)

 # Cedula, digito verificador con vector

cedula = np.anage(9)
for i in range(0, len(cedula)):
    cedula[i] = int(input(f"Ingrese {i+1} dígito de cédula: "))
print(cedula)

suma_impar = np.sum([cedula[1:8:2]])  # Suma elementos de posiciones impares

pares = cedula[0:9:2] * 2  # Elementos de posiciones multiplicados por 2
for i in range(0, len(pares)):  # Recorrer vector guardado en pares
    if pares[i] > 9:
        pares[i] -= 9
suma_par = np.sum(pares)

sum_total = suma_par + suma_impar
sum_total %= 10
if sum_total != 0:
    sum_total = 10 - sum_total
    print(f"digito verificador : {sum_total}")
else:
    print(f"Digito verificador : 0")



# Cuadrados de un numero
n = int(input("Ingrese valor: "))
print(np.sum(np.arange(1, 2*n, 2)))  # Cuadrado de un numero usando solo sumas


# Multiplicar dos numeros por sumas
a = int(input("Ingrese valor: "))
b = int(input("Ingrese valor: "))
print(f"{a} * {b} = {np.sum(np.zeros(b)+a)}")


# Factorial
num = int(input("Ingrese valor: "))
# np.arange(2, num+1) Rango
print(f"Factorial de {num}! = {np.prod(np.arange(2, num+1))}")




