num_uno = int(input("Ingrese valor: "))
num_dos = int(input("Ingrese segundo valor: "))
list_1 = []
list_2 = []
list_3 = []  # Llevara valores que al ser comparados de listas anteriores sean iguales

# Guardo en una lista los valores primos de cada número:
cont = 0
for j in range(1, num_uno+1):
     if num_uno % j == 0:
          cont += 1
          list_1.append(j)  # Añado divisores a lista

for i in range(1, num_dos+1):
     if num_dos % i == 0:
          cont += 1
          list_2.append(i)

# Comparar valores en listas
for i in range(0, len(list_1)):
    for j in range(0, len(list_2)):
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])  # Agregar a lista los valores primos en común de los dos números

maximo = max(list_3)  # Valor máximo es el máximo comun divisor entre dos números

print(f"\nDivisores comúnes de {num_uno} y {num_dos} = {list_3} \nMCD = {maximo}")

