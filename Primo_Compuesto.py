# Algoritmo para saber si un numero es primo o compuesto y su Factorización prima

numero = int(input("Ingrese valor: "))
cont = 0
lista_primos = []
for j in range(1, numero+1):
     if numero % j == 0:
          cont += 1
          lista_primos.append(j)
if cont == 2:
     print(f"{numero} Es primo")
else:
     print(f"{numero} Es compuesto")

primo_min = lista_primos[1]
primo_max = lista_primos[-2]
producto_primos = primo_max * primo_min

print(f"Valores primos de {numero} = {lista_primos} \nFactorización prima {primo_min} * {primo_max} = {producto_primos}")



# Algoritmo Primo o compuesto

numero = int(input("\nIngrese numero: "))

iteracion_mitad = int((numero**(1/2)) // 1)
cont = 0
for i in range(1, iteracion_mitad+1):
     if numero % i == 0:
          cont += 1
if cont == 1:
     print("Es primo")
else:
     print("Es compuesto")