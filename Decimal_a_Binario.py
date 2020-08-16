print("Convertir de decimal a binario")
numero = int(input("Ingrese número decimal: "))
numero_original = numero
list_binario = []
i = 2
while i == 2:
    residuo = numero % 2
    list_binario.append(residuo)
    numero //= 2
    if numero == 0:
        i = 5

lista_invertida = []
for j in range(len(list_binario)-1, -1, -1):  # Invierto lista, hasta -1 porque necesito la posición 0, paso -1
    lista_invertida.append(list_binario[j])

print(f"{numero_original} decimal a binario = {lista_invertida} base 2.")