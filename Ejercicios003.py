"""Dada una medida de tiempo expresada en horas, minutos y segundos con valores aleatorios.
    Elabore un programa que transforme dicha medida en una expresión correcta. """

horas = int(input("Ingrese horas: "))
minutos = int(input("Ingrese minutos: "))
segundos = int(input("Ingrese segundos: "))
dias = 0
if segundos > 60:
    minutos = minutos + (segundos // 60)
    segundos = segundos % 60
    print(segundos, " seg")
else:
    print(segundos, " seg")

if minutos > 60:
    horas = horas + (minutos // 60)
    minutos = minutos % 60
    print(minutos, " min")
else:
    print(minutos, " min")

print(horas, " h")

if horas > 24:
    dias = horas // 24
    print(dias, " dias")

print(f"{dias} dias {horas} horas {minutos} min {segundos} segundos")


# Con while

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

print(f"{dias} dias {horas} horas {min} min {segundos} segundos ")


# Promedio de 3 notas
n = int(input("Ingrese nota 1: "))
n2 = int(input("Ingrese nota 2: "))
n3 = int(input("Ingrese nota 3: "))
promedio = (n+n2+n3) / 3
print(promedio)

# Area de un triangulo
altura = int(input("Ingrese altura: "))
base = int(input("Ingrese base: "))
area = (base * altura) /2
print("El area es: ", area)

"""cedula = [1,7,1,4,1,3,1,3,4]
suma_impares = cedula[0]+cedula[2]+cedula[4]+cedula[6]+ cedula[8]
suma_pares = cedula[1]+cedula[3]+cedula[5]+cedula[7]
# Acceder elementos de lista
digitos_pares = cedula[1:8:2]
digitos_impares = cedula[0:9:2]"""

# Factorial
numero = int(input("Ingrese valor para calcular su factorial: "))
total = 1
for i in range(1, numero+1):
     total *= i
print(total)


# Realizar un programa que calculé el dígito verificador de la cédula ecuatoriana.

print("Introduce 8 digitos de cédula")
sumaPar = 0
sumaImpar = 0
i = 1
while i < 10:
     digitos = int(input("Introduce dígito: "))
     if i % 2 == 0:
          sumaPar += digitos
     else:
          prod = digitos * 2
     if prod > 9:
          prod -= 9
     sumaImpar += prod
     i += 1

sumaT = sumaPar + sumaImpar
mod = sumaT % 10
if mod != 0:
     mod = 10 - mod
     print(f"Dígito verificador es : {mod}")
else:
     print("Dígito verificador es: 0 ")



# Factura con descuento del 10% si su monto es mayor a $100
subtotal = 0
i = 1
while i != 0:
     total_productos = int(input("Ingrese total de productos: "))
     j = 1
     while j <= total_productos:
         producto = int(input("Valor producto : "))
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


print("Hola")