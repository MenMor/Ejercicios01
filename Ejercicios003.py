print("Dada una medida de tiempo expresada en horas, minutos y segundos con valores aleatorios."
      "\nElabore un programa que transforme dicha medida en una expresión correcta. "
      "\nCon while")

horas = int(input("Introduce horas: "))
min = int(input(" Introduce minutos: "))
segundos = int(input("Introduce segundos: "))

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

print(f"{dias} dias {horas} horas {min} min {segundos} segundos ")




print ("\nPromedio de 3 notas")
n = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))
promedio = (n+n2+n3) / 3
print(promedio)



print("\nArea de un triangulo")
altura = int(input("Ingrese altura: "))
base = int(input("Ingrese base: "))
area = (base * altura) / 2
print("El area es: ", area)




"""cedula = [1,7,1,4,1,3,1,3,4]
suma_impares = cedula[0]+cedula[2]+cedula[4]+cedula[6]+ cedula[8]
suma_pares = cedula[1]+cedula[3]+cedula[5]+cedula[7]
# Acceder elementos de lista
digitos_pares = cedula[1:8:2]
digitos_impares = cedula[0:9:2]"""



# Factorial
numero = int(input("Ingrese valor para calcular su factorial: "))
factorial = 1
for i in range(2, numero+1):
     factorial *= i
print(factorial)





# Realizar un programa que calculé el dígito verificador de la cédula ecuatoriana.

print("\nIntroduce 9 digitos de cédula")
sumaPar = 0
sumaImpar = 0
producto = 0
i = 1
while i < 10:
     digitos = int(input(f"Introduce dígito {i}: "))
     if i % 2 == 0:
          sumaPar += digitos
     else:
          producto = digitos * 2
          if producto > 9:
              producto -= 9
          sumaImpar += producto
     i += 1

sumaT = sumaPar + sumaImpar
mod = sumaT % 10
if mod != 0:
     mod = 10 - mod
     print(f"Dígito verificador es : {mod}")
else:
     print("Dígito verificador es: 0 ")


# Realizar un programa que calculé el dígito verificador de la cédula ecuatoriana. Con listas.

cedula = []
for i in range(0, 9):
    digito_in = int(input(f"Ingrese {i+1} digito de cedula: "))
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





# Factura con descuento del 10% si su monto es mayor a $100
subtotal = 0
i = 1
while i != 0:
     total_productos = int(input("Ingrese total de productos: "))
     j = 1
     while j <= total_productos:
         producto = float(input("Valor producto : "))
         subtotal += producto
         j += 1
     fin_while = int(input(" digite 0 para terminar proceso:"))
     if fin_while == 0:
          i = 0

if subtotal > 100:
    descuento = subtotal * 0.10
    subtotal -= descuento

iva = subtotal * 0.12
iva = round(iva, 2)
total_pago = subtotal + iva
total_pago = round(total_pago, 2)

print(f"IVA: {iva} Total a pagar: {total_pago}")


#Cuantos digitos tiene un numero ingresado

num = int(input("Ingrese "))
cadena = str(num)  # Convierto un numero entero a cadena string.
longitud = len(cadena)  # Longitud de cadena. Cuantos digitos tiene numero que ingreso.
print(longitud)



j = 5
x = 0
while j >= 1:
    for i in range(1, j+1):
        x += 1
        print(x, "x")
        j //= 2
        print(j, "j")


print("\n")
i = 6
x = 0
while i >= 1:
    x += 1
    print(x, "x")
    i //=2
    print(i, "i")



print("\n")
#Listas con estructuras condicionales y bucles
cubos = [i**3 for i in range(5)]
print(f"Numeros al cubo desde 0 a 5 {cubos}")

pares = [i**2 for i in range(10) if i**2 % 2 == 0]
print(f"Numeros pares desde 0 hasta 10, divisibles para 2 = {pares}")

#Lista multiples de 3 desde 0 hasta 20

multiplos_3 = [i for i in range(20) if i % 3 == 0]
print(f"Multiplos de 3 = {multiplos_3}")

# Lista de valores pares
par = [2*i for i in range(3*4)]
print(par)

#Lista de valores elevados al cubo
cubos = [3*i for i in range(5*5)]
print(cubos)

#Funcion format. Cambia valores que estan entre llaves {} de una cadena con los asignados de una lista
nums = [4, 5, 6]
msg = "Numbers : {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# Funcion join. Pone el caracter deseado en medio de los elementos de lista
print(",1". join(["spam", "huevos", "jamón"]))




"""print("\n")
t = [0, 9, 0, 0, 0, 1]
p = t[1]
print(p)"""


"""n = float(input("I "))
k = n // 1
print(k)"""


# Primo o compuesto
num_p= int(input("Ingrese valor: "))
cont = 0
for j in range(2, num_p+1):
     if num_p % j == 0:
          cont += 1
          print(j)
if cont == 2:
     print("Es primo")
else:
     print("Es compuesto")




num_uno = []
for i in range(len(vector_uno)-1, -1, -1):
    num_uno.append(vector_uno[i])

num_dos = []
for j in range(len(vector_dos)-1, -1, -1):
    num_dos.append(vector_dos[j])


