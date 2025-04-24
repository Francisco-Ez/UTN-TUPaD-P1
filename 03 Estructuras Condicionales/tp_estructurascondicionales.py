#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("Escriba su edad")
edad= int(input())

if edad > 18:
   print("Es mayor de edad")
else:
   pass

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

print("Escriba su nota")
nota= int(input())

if nota >= 6:
 print("Aprobado")
else:
 print("Desaprobado")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print("Ingrese un numero par")
numero= int(input())

if numero % 2==0:
 print("ha ingresado un número par")
else:
 print("por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.


print("Ingrese su edad")
edad= int(input())

if edad < 12:
 print("Perteneces a la categoria niño/a")
elif edad >= 12 and edad < 18:
 print("Perteneces a la categoria adolescente")
elif edad >=18 and edad <30:
 print("Perteneces a la categoria adulto/a joven")
elif edad >= 30:
 print("Perteneces a la categoria adulto/a")
else:
 print("Error. Vuelva a ingresar su edad")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

print("Ingrese su contraseña")
contraseña= input()
tamaño_contraseña= len(contraseña)

if tamaño_contraseña >=8 and tamaño_contraseña <=14:
 print("Ha ingresado una contraseña correcta")
else:
 print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)

import statistics
import random
numeros_aleatorios= {random.randint(1,100) for i in range(50)}
print(numeros_aleatorios)
valor_media= statistics.mean(numeros_aleatorios)
print (f"el valor de media (mean) es {valor_media}")
valor_mediana= statistics.median(numeros_aleatorios)
print (f"el valor de la mediana (median) es {valor_mediana}")
valor_moda= statistics.mode(numeros_aleatorios)
print(f"el valor de la moda (mode) es {valor_moda}")

if valor_media > valor_mediana and valor_mediana > valor_moda:
    print("Hay sesgo positivo ")
elif valor_media < valor_mediana and valor_mediana < valor_moda:
    print("Hay sesgo negativo")
elif valor_media == valor_mediana == valor_moda:
    print("No hay sesgo")
else:
    pass

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

print("Escriba una frase o palabra")
frase_palabra= input()
caracter= frase_palabra[-1]


if caracter in "aeiou":
    print(f"{frase_palabra}!")
else:
    print(frase_palabra)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas

print("Ingrese su nombre")
nombre= input()
print("Eliga una opción:\n ingrese 1 Si quiere su nombre en mayusculas. Por ejemplo: PEDRO \n Ingrese 2 Si quiere su nombre en minúsculas. Por ejemplo: pedro \n Ingrese 3 Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
opcion= input()

if opcion == "1":
    nombre=nombre.upper()
    print(nombre)
elif opcion=="2":
   nombre=nombre.lower()
   print(nombre)
elif opcion=="3":
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


print("Escriba la magnitud del terremoto")
magnitud= int(input())

if magnitud < 3:
   print("La magnitud es muy leve (imperceptible)")

elif magnitud >= 3 and magnitud < 4:
   print("La magnitud es leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
   print("La magnitud es moderada (sentida por personas, pero generalmente no causa daños) ")
elif magnitud >= 5 and magnitud < 6:
   print("La magnitud es fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
   print("La magnitud es muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
   print("La magnitud es extrema (puede causar graves daños a gran escala)")
else:
    pass

#10)
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("¿En que hemisferio ese encuentra? (N/S)").upper()
mes= int(input("Qué mes es? (1-12)"))
dia= int(input("¿Qué día es?(1-31)"))
estacion=0

if hemisferio=="N":
  if(mes==12 and dia >= 21) or (1<= mes <= 2) or (mes==3 and dia <20):
    estacion="invierno"
  elif(mes == 3 and dia >= 20) or (4 <=mes <= 5) or (mes == 3 and dia <20):
    estacion= "primavera"
  elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 22):
    estacion= "verano"
  elif(mes == 9 and dia >= 23) or (10 <= mes <= 11 ) or (mes == 12 and dia <21):
    estacion= "otoño"

elif hemisferio=="S":
 if(mes == 6 and dia >= 21) or (7 <= mes <= 8 ) or (mes == 9 and dia <22):
   estacion= "invierno"
 elif (mes == 9 and dia >= 22) or (10<= mes <= 11 ) or (mes == 12 and dia <21):
   estacion= "primavera"
 elif (mes == 12 and dia >= 21) or (1 <= mes <= 2 ) or (mes == 3 and dia <20):
   estacion= "verano"
 elif (mes == 3 and dia >= 20) or (4 <= mes <= 5 ) or (mes == 6 and dia <21):
   estacion= "otoño"
else:
  estacion="hemisferio no válido"

print(f"Usted se encuentra en {estacion}")
  


