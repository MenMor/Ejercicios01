# Encontrar máximo común divisor (mcd), entre dos números

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
if cont == 2:  # Comparo para saber si es primo o sino es compuesto
     print(f"\n{num_uno} Es primo")
else:
     print(f"\n{num_uno} Es compuesto")
print(f"Divisores de {num_uno} = {list_1}")

for i in range(1, num_dos+1):
     if num_dos % i == 0:
          cont += 1
          list_2.append(i)
if cont == 2:
     print(f"\n{num_dos} Es primo")
else:
     print(f"\n{num_dos} Es compuesto")
print(f"Divisores de {num_dos} = {list_2}")


for i in range(0, len(list_1)):  # Recorrera todas las posiciones de lista 1
    for j in range(0, len(list_2)):  # Con todas la posiciones de lista 2
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])
maximo = max(list_3)  # Máximo es el mcd
print(f"\nDivisores comúnes de {num_uno} y {num_dos} = {list_3} \nmcd({num_uno},{num_dos})= {maximo}")
