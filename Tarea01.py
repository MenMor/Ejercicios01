import math

# Convertir de grados a radianes.
print("Convertir de grados a radianes.")

grados = int(input("Ingrese valor de grados a convertir: "))
rad = grados * math.pi / 180
print(f"Grados {grados} a {rad} rad")

"""print("Grados", grados, " a ", rad, " rad")
   print(grados * 3.1416 / 180, "rad")"""







""" Realizar un algoritmo que pida al usuario la velocidad en m/s y el radio de la
    circunferencia de la pista, el resultado el programa devuelve el tiempo que tarda el
    atleta en dar dos vueltas a la pista, sabiendo que el atleta descansa 1min cada 1000m. """

print("\n Cálculo de tiempo que tarda un atelta en dar dos vueltas a la pista.")

velocidad = float(input("Introduce velocidad en m/s: "))
radio = float(input("Introduce radio de pista: "))

velocidad_angular = velocidad/radio  # velocidad angular para fórmula periodo de mcu.
tiempo = (2 * math.pi / velocidad_angular) * 2
longitud = (2 * math.pi * radio) / 1000

if longitud > 1:  # Descanso n veces mayores a 1000
    n = longitud/1000  # Longitud con respecto a 1000 metros
    tiempo *= n  # tiempo multiplicado por la razon respecto a longitud

print(f"Tiempo : {round(tiempo, 2)} ")








""" Elaborar un algoritmo que calculé el impuesto a la renta con relación de dependencia de un empleado,
    conociendo el sueldo mensual del funcionario, sus gastos deducibles del año (Salud, vivienda, alimentación, 
    educación y vestimenta) y el porcentaje de aportación al IESS. Debe basarse en la tabla de Impuesto a la Renta 
    del 2020 para si cálculo."""

print("\n Cálculo impuesto a la renta con relación de dependencia de un empleado.")

sueldo = float(input("Introduce sueldo mensual de funcionario  "))
gastos = float(input("Introduce total de gastos de Salud, vivienda, alimentación, educación y vestimenta  "))

if gastos <= sueldo*0.5:  # La deducción total por gastos personales no podrá superar el 50% del total de los ingresos

    sueldo *= 12  # 12 meses
    aporte_iess = sueldo * 0.0945  # Aporte iess personal 9,45 %
    aporte_iess = (round(aporte_iess, 2))  # Redondeo y limito a dos decimales
    sueldo = sueldo - aporte_iess - gastos  # Resto fraccion basica
    sueldo = (round(sueldo, 2))

    if sueldo <= 11315.00:
        impuesto = 0

    elif (sueldo >= 11315.01) and (sueldo <= 14416.00):
        impuesto = sueldo * 0.05

    elif (sueldo >= 14416.01) and (sueldo <= 18018.00):
        impuesto = sueldo * 0.10 + 155

    elif (sueldo >= 18018.01) and (sueldo <= 21639.00):
        impuesto = sueldo * 0.12 + 515

    elif (sueldo >= 21639.01) and (sueldo <= 43268.00):
        impuesto = sueldo * 0.15 + 950

    elif (sueldo >= 43268.01) and (sueldo <= 64887.00):
        impuesto = sueldo * 0.20 + 4194

    elif (sueldo >= 64887.01) and (sueldo <= 86516.00):
        impuesto = sueldo * 0.25 + 8518

    elif (sueldo >= 86516.01) and (sueldo <= 115338.00):
        impuesto = sueldo * 0.30 + 13925

    else:
        impuesto = sueldo * 0.35 + 22572

    impuesto = round(impuesto, 2)  # Limito a 2 decimales
    print(f"Impuesto a la renta: {impuesto}")

else:
    print("Los gastos superan a sus ingresos.")








# Resolucion ecuacion cuadratica ax^2 + bx + c = 0 por formula general

print("\nResolución ecuación cuadratica ax^2 + bx + c = 0 por formula general.")
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

discriminante = b ** 2 - 4 * a * c

if discriminante < 0:
    print("La ecuación no tiene soluciones reales")
elif discriminante == 0:
    x = -b / 2*a
    print(f"Solución unica: {x}")
else:
    x1 = (-b - math.sqrt(discriminante)) / (2*a)
    x2 = (-b + math.sqrt(discriminante)) / (2*a)
    print(f"Dos soluciones reales: x1= {x1} x2= {x2}")








"""Dada una medida de tiempo expresada en horas, minutos y segundos con valores aleatorios.
   Elabore un programa que transforme dicha medida en una expresión correcta."""

print("\nMedida de tiempo.")

horas = int(input("Ingrese horas: "))
minutos = int(input("Ingrese minutos: "))
segundos = int(input("Ingrese segundos: "))
dias = 0
if segundos > 60:
    minutos = minutos + segundos // 60
    segundos %= 60

else:
    print(segundos, " seg")

if minutos > 60:
    horas = horas + minutos // 60
    minutos %= 60

else:
    print(minutos, " min")


if horas > 24:
    dias = horas // 24

print(f"{dias} dias {horas} horas {minutos} min {segundos} segundos")








# Factura con descuento del 10% si su monto es mayor a $100

print("\nFactura con descuento del 10% si su monto es mayor a $100.")

producto1 = float(input("Valor producto 1: "))
producto2 = float(input("Valor producto 2: "))
producto3 = float(input("Valor producto 3: "))

subtotal = producto1 + producto2 + producto3
if subtotal > 100:
    descuento = subtotal * 0.10
    subtotal -= descuento

iva = subtotal * 0.12
iva = round(iva, 2)  # redondeo y limito a 2 decimales
total_pago = subtotal + iva
total_pago = round(total_pago, 2)
print(f"IVA: {iva} Total a pagar: {total_pago}")








# Si el promedio es mayor a 7 el alumno esta aprobaado caso contario estara reprobado

print("\nPromedio")

nota1 = float(input("Ingrese primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))

promedio = (nota1 + nota2) / 2

if promedio >= 7:
     print(f"Materia aprobada {promedio}")
else:
     print(f"Materia Reprobada {promedio}")








# algoritmo que simula una calculadora basica (menu para que usuario indique que operacion desea)
print("\nCalculadora básica; elija su opción.")

opcion = int(input("1. Suma" "\n2. Resta" "\n3. Multiplicación" "\n4. División" "\n:  "))

if (opcion == 1) or (opcion == 2) or (opcion == 3) or (opcion == 4):

    numero1 = float(input("Ingrese primer valor: "))
    numero2 = float(input("Ingrese segundo valor: "))
    resultado = 0

    if opcion == 1:
        resultado = numero1 + numero2
        print("Respuesta: ", resultado)

    elif opcion == 2:
        resultado = numero1 - numero2
        print("Respuesta: ", resultado)

    elif opcion == 3:
        resultado = numero1 * numero2
        print("Respuesta: ", resultado)

    else:
        if numero2 == 0:
            print("Error división sobre 0")
        else:
            resultado = numero1 / numero2
            print("Respuesta: ", resultado)

else:
    print("No existe esa opción")








print("\nAlgoritmo que determina si un numero entero es divisible para otro")

numero_uno = int(input("Ingrese primer número: "))
numero_dos = int(input("Ingrese segundo número: "))

divisible = numero_uno % numero_dos

if divisible == 0:
    print("Es divisible: ", numero_uno / numero_dos)
else:
    print("No es divisible")








print("\nRealizar un programa que calculé el dígito verificador de la cédula ecuatoriana.")

cedula = [1, 7, 1, 6, 0, 8, 5, 5, 8]

cedula[0] = cedula[0] * 2
if cedula[0] > 9:
    cedula[0] -= 9

cedula[2] = cedula[2] * 2
if cedula[2] > 9:
    cedula[2] -= 9

cedula[4] = cedula[4] * 2
if cedula[4] > 9:
    cedula[4] -= 9

cedula[6] = cedula[6] * 2
if cedula[6] > 9:
    cedula[6] -= 9

cedula[8] = cedula[8] * 2
if cedula[8] > 9:
    cedula[8] -= 9

suma_pares = cedula[1]+cedula[3]+cedula[5]+cedula[7]

suma_impares = cedula[0] + cedula[2] + cedula[4] + cedula[6] + cedula[8]

suma_total = suma_pares + suma_impares

suma_total %= 10
if suma_total != 0:
    suma_total = 10 - suma_total
    print(f"Dígito verificador es: {suma_total}")
else:
    print(f"Dígito verificandor es : {suma_total}")
