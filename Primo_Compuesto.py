# Algoritmo para saber si un numero es primo o compuesto y su desco,posicion de factores



numero = int(input("Ingrese valor: "))
cont = 0
lista_primos = []
for j in range(1, numero+1):  # No incluyo extremos
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


