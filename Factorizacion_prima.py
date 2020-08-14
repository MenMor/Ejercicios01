"""El teorema fundamental de la Aritmética establece que cada número natural mayor que 1 puede ser
   escrito como un producto de números primos ,y eso hasta el rearreglo de los factores,
   este producto es único . Esto es llamada la factorización prima del número"""
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





# Factorización prima de un valor factorial. EFICIENTE

print("\nFactorización prima de un valor factorial")

numero = int(input("Ingrese valor para calcular su factorización prima: "))
factorial = 1
for i in range(2, numero+1):
     factorial *= i
print(f"Factorial de {numero}! = {factorial}")

list_divisores = []
cont = 0
for j in range(1, factorial+1):
     if factorial % j == 0:
          cont += 1
          list_divisores.append(j)
if cont == 2:
     print(f"Es primo \nDivisores: {list_divisores}")
else:
     print(f"Es compuesto \nDivisores: {list_divisores}")

desde = (len(list_divisores)) // 2
division = factorial / list_divisores[desde]
prod = division * list_divisores[desde]
print(f"DescomposiciÓn prima = {division} * {list_divisores[desde]} = {prod}")





# primo = int(primo ** (1/2) // 2) Recortar iteraciones a la mitad

# Factorización prima de un valor factorial

print("\nFactorización prima de un valor factorial")

numero = int(input("Ingrese valor para calcular su factorización prima: "))
factorial = 1
for i in range(2, numero+1):
     factorial *= i
print(f"Factorial de {numero}! = {factorial}")

list_divisores = []
cont = 0
for j in range(1, factorial+1):
     if factorial % j == 0:
          cont += 1
          list_divisores.append(j)

# Buscar entre necesito
numero_n = int((numero ** (1/2)) // 1)
desde = numero_n // 2
for i in range(desde, numero_n):
     if list_divisores[i] <= numero_n:
          x = list_divisores[i]
          divisor = factorial/x
          prod = divisor * x
          if prod == factorial:
               print(f"Descomposición primos {divisor} * {x} = {prod} ")
if cont == 2:
     print(f"Es primo \nDivisores: {list_divisores}")
else:
     print(f"Es compuesto \nDivisores: {list_divisores}")



