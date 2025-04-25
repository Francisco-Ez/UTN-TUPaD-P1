#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Mostramos un mensaje solicitando al usuario que ingrese su edad
print("Escriba su edad")
# Leemos la edad ingresada por el usuario y la convertimos a entero
edad= int(input())
# Verificamos si la edad es mayor a 18
if edad > 18:
   # Si la condición se cumple, se imprime que es mayor de edad
   print("Es mayor de edad")
else:
   # Si la edad no es mayor a 18, no se realiza ninguna acción
    # El uso de 'pass' indica que no se hace nada en este caso
   pass



#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

# Solicitamos al usuario que ingrese su nota
print("Escriba su nota")
# Leemos la nota desde la entrada estándar y la convertimos a un número entero
nota= int(input())
# Verificamos si la nota es mayor o igual a 6 (nota mínima para aprobar)
if nota >= 6:
 # Si la condición se cumple, el estudiante está aprobado
 print("Aprobado")
else:
 # Si la nota es menor a 6, el estudiante está desaprobado
 print("Desaprobado")



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# Solicitamos al usuario que ingrese un número par
print("Ingrese un numero par")
# Leemos el número ingresado por el usuario y lo convertimos a entero
numero= int(input())
# Verificamos si el número es par (su residuo al dividirlo entre 2 es cero)
if numero % 2==0:
 # Si es par, se muestra un mensaje de confirmación
 print("ha ingresado un número par")
else:
# Si no es par, se solicita que ingrese un número par
 print("por favor, ingrese un número par")



#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

# Solicitamos al usuario que ingrese su edad
print("Ingrese su edad")
# Leemos la edad ingresada por el usuario y la convertimos a un número entero
edad= int(input())
# Clasificamos al usuario según su edad

# Si la edad es menor a 12 años
if edad < 12:
 print("Perteneces a la categoria niño/a")
# Si la edad es de 12 a 17 años inclusive
elif edad >= 12 and edad < 18:
 print("Perteneces a la categoria adolescente")
# Si la edad es de 18 a 29 años inclusive
elif edad >=18 and edad <30:
 print("Perteneces a la categoria adulto/a joven")
# Si la edad es 30 o más
elif edad >= 30:
 print("Perteneces a la categoria adulto/a")
# Este bloque se ejecutará si se ingresa un valor que no encaja en ninguna categoría
else:
 print("Error. Vuelva a ingresar su edad")



#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

# Solicitamos al usuario que ingrese su contraseña
print("Ingrese su contraseña")
# Leemos la contraseña ingresada por el usuario
contraseña= input()
# Calculamos la longitud de la contraseña ingresada
tamaño_contraseña= len(contraseña)
# Verificamos si la longitud de la contraseña está entre 8 y 14 caracteres
if tamaño_contraseña >=8 and tamaño_contraseña <=14:
 # Si la contraseña tiene una longitud válida (entre 8 y 14 caracteres), mostramos un mensaje de éxito
 print("Ha ingresado una contraseña correcta")
else:
 # Si la contraseña tiene una longitud fuera de este rango, solicitamos que ingrese una nueva contraseña
 print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)

# Importamos la librería 'statistics' para realizar cálculos estadísticos
import statistics
# Importamos la librería 'random' para generar números aleatorios
import random
# Generamos un conjunto de 50 números aleatorios entre 1 y 100 (el conjunto elimina duplicados)
numeros_aleatorios= {random.randint(1,100) for i in range(50)}
# Mostramos el conjunto de números aleatorios generados
print(numeros_aleatorios)
# Calculamos la media (promedio) de los números aleatorios usando la función 'mean' de la librería 'statistics'
valor_media= statistics.mean(numeros_aleatorios)
# Mostramos el valor de la media calculada
print (f"el valor de media (mean) es {valor_media}")
# Calculamos la mediana de los números aleatorios usando la función 'median' de 'statistics'
valor_mediana= statistics.median(numeros_aleatorios)
# Mostramos el valor de la mediana calculada
print (f"el valor de la mediana (median) es {valor_mediana}")
# Calculamos la moda (el número más frecuente) de los números aleatorios usando la función 'mode' de 'statistics'
valor_moda= statistics.mode(numeros_aleatorios)
# Mostramos el valor de la moda calculada
print(f"el valor de la moda (mode) es {valor_moda}")

# Analizamos si existe algún sesgo en los datos comparando la media, mediana y moda
if valor_media > valor_mediana and valor_mediana > valor_moda:
    # Si la media es mayor que la mediana y la mediana es mayor que la moda, hay sesgo positivo
    print("Hay sesgo positivo ")
elif valor_media < valor_mediana and valor_mediana < valor_moda:
    # Si la media es menor que la mediana y la mediana es menor que la moda, hay sesgo negativo
    print("Hay sesgo negativo")
elif valor_media == valor_mediana == valor_moda:
    # Si la media, mediana y moda son iguales, no hay sesgo
    print("No hay sesgo")
else:
    # Si no se cumple ninguna de las condiciones anteriores, no se hace nada
    pass



#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

# Solicitamos al usuario que escriba una frase o una palabra
print("Escriba una frase o palabra")
frase_palabra= input()
# Leemos la entrada del usuario y la guardamos en la variable 'frase_palabra'
caracter= frase_palabra[-1]

# Verificamos si el último carácter es una vocal minúscula
if caracter in "aeiou":
   # Si termina en vocal, mostramos la palabra seguida de un signo de exclamación
    print(f"{frase_palabra}!")
else:
   # Si no termina en vocal, se imprime tal cual fue ingresada
    print(frase_palabra)



#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas

# Solicitamos al usuario que ingrese su nombre
print("Ingrese su nombre")
nombre= input()
# Presentamos un menú con 3 opciones de formato para mostrar el nombre
print("Eliga una opción:\n ingrese 1 Si quiere su nombre en mayusculas. Por ejemplo: PEDRO \n Ingrese 2 Si quiere su nombre en minúsculas. Por ejemplo: pedro \n Ingrese 3 Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
# Leemos la opción elegida por el usuario
opcion= input()
# Según la opción seleccionada, aplicamos el formato correspondiente
if opcion == "1":
   # Convertimos el nombre a mayúsculas con .upper()
    nombre=nombre.upper()
    print(nombre)
elif opcion=="2":
   # Convertimos el nombre a minúsculas con .lower()
   nombre=nombre.lower()
   print(nombre)
elif opcion=="3":
   # Convertimos la primera letra de cada palabra a mayúscula con .title()
    nombre=nombre.title()
    print(nombre)



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

# Solicitamos al usuario que ingrese la magnitud de un terremoto (como un número entero)
print("Escriba la magnitud del terremoto")
magnitud= int(input())
# Evaluamos el nivel de intensidad del terremoto según su magnitud en la escala de Richter

# Si la magnitud es menor que 3, se considera imperceptible
if magnitud < 3:
   print("La magnitud es muy leve (imperceptible)")
# Si la magnitud está entre 3 y 3.9
elif magnitud >= 3 and magnitud < 4:
   print("La magnitud es leve (ligeramente perceptible)")
# Si la magnitud está entre 4 y 4.9
elif magnitud >= 4 and magnitud < 5:
   print("La magnitud es moderada (sentida por personas, pero generalmente no causa daños) ")
# Si la magnitud está entre 5 y 5.9
elif magnitud >= 5 and magnitud < 6:
   print("La magnitud es fuerte (puede causar daños en estructuras débiles)")
# Si la magnitud está entre 6 y 6.9
elif magnitud >= 6 and magnitud < 7:
   print("La magnitud es muy fuerte (puede causar daños significativos)")
# Si la magnitud es 7 o mayor
elif magnitud >= 7:
   print("La magnitud es extrema (puede causar graves daños a gran escala)")
# Si incluye el bloque else con  'pass' para mantener la estructura completa
else:
    pass



#10)
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitamos al usuario que indique en qué hemisferio se encuentra (Norte o Sur)
# Convertimos la entrada a mayúsculas para asegurar uniformidad en la comparación
hemisferio= input("¿En que hemisferio ese encuentra? (N/S)").upper()
# Pedimos al usuario que indique el mes actual como un número del 1 al 12
mes= int(input("Qué mes es? (1-12)"))
# Pedimos también el día del mes
dia= int(input("¿Qué día es?(1-31)"))
# Inicializamos la variable estación
estacion=0
# Determinamos la estación si el hemisferio es Norte
if hemisferio=="N":
    # Invierno: desde el 21 de diciembre hasta antes del 20 de marzo
  if(mes==12 and dia >= 21) or (1<= mes <= 2) or (mes==3 and dia <20):
    estacion="invierno"
    # Primavera: desde el 20 de marzo hasta antes del 21 de junio
  elif(mes == 3 and dia >= 20) or (4 <=mes <= 5) or (mes == 3 and dia <20):
    estacion= "primavera"
   # Verano: desde el 21 de junio hasta antes del 23 de septiembre
  elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 22):
    estacion= "verano"
   # Otoño: desde el 23 de septiembre hasta antes del 21 de diciembre
  elif(mes == 9 and dia >= 23) or (10 <= mes <= 11 ) or (mes == 12 and dia <21):
    estacion= "otoño"
     
# Determinamos la estación si el hemisferio es Sur
elif hemisferio=="S":
 # Invierno: desde el 21 de junio hasta antes del 22 de septiembre
 if(mes == 6 and dia >= 21) or (7 <= mes <= 8 ) or (mes == 9 and dia <22):
   estacion= "invierno"
 # Primavera: desde el 22 de septiembre hasta antes del 21 de diciembre
 elif (mes == 9 and dia >= 22) or (10<= mes <= 11 ) or (mes == 12 and dia <21):
   estacion= "primavera"
 # Verano: desde el 21 de diciembre hasta antes del 20 de marzo
 elif (mes == 12 and dia >= 21) or (1 <= mes <= 2 ) or (mes == 3 and dia <20):
   estacion= "verano"
 # Otoño: desde el 20 de marzo hasta antes del 21 de junio
 elif (mes == 3 and dia >= 20) or (4 <= mes <= 5 ) or (mes == 6 and dia <21):
   estacion= "otoño"
 # Si el usuario no ingresó un hemisferio válido (ni "N" ni "S")
else:
  estacion="hemisferio no válido"
# Mostramos la estación correspondiente según el mes, el día y el hemisferio
print(f"Usted se encuentra en {estacion}")
  


