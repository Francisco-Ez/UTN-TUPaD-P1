#1.Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

# Función que imprime el mensaje "Hola mundo!" en pantalla
def imprimir_hola_mundo():
   print("Hola mundo!")

# Llamada a la función desde el programa principal
imprimir_hola_mundo()



#2.Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"),
#deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

# Función que recibe un nombre y devuelve un saludo personalizado
def saludar_usuario(nombre):
    mensaje=f"Hola {nombre}!"
    return mensaje

# Solicita el nombre al usuario
nombre=input("Escriba su nombre para recibir un saludo: ")

# Muestra el saludo por pantalla
print(saludar_usuario(nombre))



#3.Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[#nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Función que devuelve una frase con información personal
def informacion_personal(nombre,apellido,edad,residencia):
        resultado= f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
        return resultado

# Solicita los datos personales al usuario
nombre=input("Escriba su nombre: ")
apellido=input("Escriba su apellido: ")
edad=input("Escriba su edad: ")
residencia=input("Escriba su residencia: ")

# Muestra la información personal por pantalla
print(informacion_personal(nombre, apellido, edad, residencia))



#4.Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
#como parámetro y devuelva el área del círculo.
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
#devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Función para calcular el área de un círculo dado su radio
def calcular_area_circulo(radio):
    area= 3.14159 * (radio*radio)
    return area

# Función para calcular el perímetro de un círculo dado su radio
def calcular_perimetro_circulo(radio):
    perimetro= 2* 3.14159 * radio
    return perimetro

# Solicita el radio al usuario
radio=int(input("Escriba el radio: "))

# Muestra área y perímetro calculados
print(f"El area del circulo es {calcular_area_circulo(radio)}")

print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)}")



#5.Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar 
#el resultado usando esta función

# Función que convierte una cantidad de segundos a horas (enteras)
def segundos_a_horas(segundos):
    horas= segundos // 3600 # División entera
    return horas

# Solicita los segundos al usuario
segundos=int(input("Escriba los segundos: "))

# Muestra la conversión a horas
print(f"{segundos} segundos son : {segundos_a_horas(segundos)} hora")



#6.Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Función que imprime la tabla de multiplicar del 1 al 10 de un número dado
def tabla_multiplicar(numero):
        for i in range(1, 11):
            multiplicacion= numero*i
            print(f"{numero} x {i} = {multiplicacion}")
            
# Solicita el número al usuario   
numero=int(input("Escriba un número para que el programa muestre su tabla de multiplicar: "))

# Muestra la tabla de multiplicar
tabla_multiplicar(numero)



#7.Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

# Función que realiza operaciones básicas y devuelve los resultados en una tupla
def operaciones_basicas(a, b):
    mi_lista=[]
    mi_lista.append(a+b)   # Suma
    mi_lista.append(a-b)   # Resta
    mi_lista.append(a*b)   # Multiplicación
    mi_lista.append(a/b)   # División
    tupla=tuple(mi_lista)
    return tupla

# Solicita dos números al usuario
a=int(input("Escriba el primer número "))
b=int(input("Escriba el segundo número "))

# Muestra los resultados de las operaciones
print(f"Suma, resta, multiplicación y división entre {a} y {b}: {operaciones_basicas(a,b)}")



#8.Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.

# Función que calcula el índice de masa corporal (IMC) dado peso y altura
def calcular_imc(peso, altura):
    imc= peso/(altura*altura)
    return round(imc,2)   # Se redondea a 2 decimales

# Solicita datos al usuario
altura=float(input("Escriba su altura en metros "))
peso=int(input("Escriba su peso en kilogramos "))

# Muestra el IMC calculado
print(f"El IMC es {calcular_imc(peso,altura)}")



#9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

# Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
     fahrenheit= (celsius * 1.8) + 32
     return  fahrenheit

# Solicita la temperatura en Celsius al usuario
celsius=float(input("Escriba una temperatura en grados celsius "))

# Muestra la conversión a Fahrenheit
print(f"{celsius} grados celsius es equivalente a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")



#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

# Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return round(promedio,2)

# Solicita los tres números al usuario
a=int(input("Escriba el primer número para calcular el promedio: "))
b=int(input("Escriba el segundo número para calcular el promedio: "))
c=int(input("Escriba el tercer número para calcular el promedio: "))

# Muestra el promedio
print(calcular_promedio(a,b,c))