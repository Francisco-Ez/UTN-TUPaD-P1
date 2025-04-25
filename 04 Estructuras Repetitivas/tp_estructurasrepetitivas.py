#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Inicializamos la variable 'numero' con el valor 0
# Esta variable servirá como contador en nuestro bucle
numero=0
# Iniciamos un bucle while que se ejecutará mientras 'numero' sea menor o igual a 100
while numero <=100:
# Imprimimos el valor actual de 'numero' en la consola
    print(numero)
# Incrementamos el valor de 'numero' en 1 para avanzar en el conteo
    numero= numero+1




#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

# Mostramos un mensaje solicitando al usuario que escriba un número entero
print("Escriba un número entero")
# Leemos la entrada del usuario, la convertimos a entero y la guardamos en la variable 'numero'
numero= int(input())
# Inicializamos el contador en 1 porque cualquier número entero tiene al menos un dígito
contador=1
# Mientras el número sea mayor o igual a 10, seguimos dividiéndolo por 10
# Esto reduce el número y nos permite contar cuántas veces se puede dividir por 10 antes de ser menor que 10
while numero >=10:
   numero= numero/ 10  # Dividimos entre 10 para "eliminar" un dígito
   contador+= 1        # Aumentamos el contador de dígitos
# Mostramos el número total de dígitos usando una f-string para insertar el valor del contador
print(f"El numero tiene {contador} digitos")




#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Inicializamos el contador y la suma en 0
contador=0
suma=0
# Solicitamos al usuario que ingrese el primer número
print("Escriba el primer número")
num1= int(input())   # Leemos el primer número como un entero
# Solicitamos al usuario que ingrese el segundo número
print("Escriba el segundo número")
num2= int(input())   # Leemos el segundo número como un entero

# Entramos en un bucle que continuará mientras 'num1' no sea igual a 'num2 - 1'
# Es decir, el bucle se ejecutará mientras num1 sea menor que num2
while not num1 == num2-1:
    # Asignamos a 'contador' el siguiente número después de 'num1'
    contador= num1+1
    # Sumamos el valor de 'contador' a 'suma'
    suma= suma+contador
    # Incrementamos 'num1' en 1 para continuar el proceso
    num1+=1
# Al final del bucle, mostramos la suma acumulada
print(suma)



#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

# Inicializamos la variable 'suma' en 0 para guardar el total acumulado
suma=0
# Convertimos la entrada del usuario a un número entero y la almacenamos en 'num1'
num1=1
# Bucle que se repite mientras el número ingresado no sea 0
while num1 != 0:
 # Solicitamos al usuario que ingrese un número. Si ingresa 0, se termina el bucle.
 print ("Ingrese un número para añadirlo a la suma. Escriba 0 para mostrar el total acumulado ")
 # Convertimos la entrada del usuario a un número entero y la almacenamos en 'num1'
 num1= int(input())
 # Sumamos el número ingresado a la variable 'suma'
 suma= suma + num1
 # Mostramos la suma actual después de cada número ingresado
 print(f"Suma actual: {suma}")
# Una vez que el usuario ingresa 0, se sale del bucle y se muestra la suma total
print(f"Suma final: {suma}")



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Importamos el módulo 'random' para poder generar un número aleatorio
import random
# Inicializamos la variable 'num' en 0; esta variable almacenará los intentos del usuario
num=0
# Inicializamos el contador de intentos en 0
contador=0
# Generamos un número aleatorio entre 0 y 9 que el usuario deberá adivinar	
respuesta= random.randint(0,9)
# Iniciamos un bucle que se ejecuta mientras el número ingresado por el usuario sea diferente a la respuesta	
while num != respuesta:
 # Solicitamos al usuario que intente adivinar el número
 print("Adivine el número del 0 al 9")
 # Leemos la entrada del usuario y la convertimos a entero
 num= int(input())
  # Aumentamos el contador en 1 para registrar el intento
 contador= contador+1
# Cuando el usuario adivina correctamente, se sale del bucle y se imprime un mensaje de felicitación	
print(f"Felicidades, el número era {respuesta}  Necesitaste  {contador} intentos para resolverlo.")



#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

# Inicializamos la variable 'cantidad' con 100 (aunque luego se sobrescribe en el bucle)
cantidad=100
# Iniciamos un bucle 'for' que recorre los números desde 98 hasta 2 (inclusive), en decrementos de 2
# Esto genera solo números pares en orden descendente
for cantidad in range(98,1,-2):
    # Verificamos si el número actual es par (aunque siempre lo será con este rango y paso)
    if cantidad % 2 ==0:
    # Si es par, lo imprimimos en pantalla
        print(cantidad)
    else:
    # Si por alguna razón no es par (lo cual no ocurre aquí), no hacemos nada
        pass



#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

# Solicitamos al usuario que ingrese un número entero y lo guardamos en 'num1'
num1= int(input("Escriba un número "))
# Inicializamos 'num2' en 0. Aunque se sobrescribirá en el bucle, se declara aquí por claridad
num2=0
# Inicializamos 'suma' en 0 para acumular la suma de los números
suma=0
# Usamos un bucle for para recorrer los números desde 0 hasta (num1 - 1)
for num2 in range(0,num1,1):
    # Sumamos cada número del rango a la variable 'suma'
    suma= suma + num2
# Una vez terminado el bucle, mostramos la suma total de los números entre 0 y num1 (excluyendo num1)
print(f"La suma de todos los números entre 0 y {num1}  es: {suma}")



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicializamos todas las variables necesarias para los contadores
cantidad=0     # Cantidad de números que el usuario desea ingresar
num=0          # Número ingresado por el usuario en cada iteración  
pares=0        # Contador de números pares
numPositivos=0 # Contador de números positivos
impares=0      # Contador de números impares
numNegativos=0 # Contador de números negativos
contador=0     # Contador de iteraciones o cantidad de números leídos

# Solicitamos al usuario que ingrese cuántos números quiere introducir (máximo 100)
print ("Escriba la cantidad de números que va a ingresar, máximo 100")
cantidad= int(input())
# Validamos que la cantidad no supere el límite establecido
if cantidad >100:
	print("ERROR, la cantidad de números debe ser menor que 100")
# Si la cantidad es válida (menor que 100), iniciamos la lectura de los números
elif cantidad <100:
 while contador != cantidad:
  print("Escriba un número")
  num= int(input())
  # Caso 1: número par y positivo
  if num % 2==0 and num > 0 :
   pares= pares+1
   numPositivos=numPositivos+1
   contador=contador+1
  # Caso 2: número impar y negativo 
  elif num %2 !=0 and num <0 :
   impares=impares+1
   numNegativos=numNegativos+1
   contador=contador+1
  # Caso 3: número par y negativo 
  elif num % 2==0 and num < 0:
   pares=pares+1
   numNegativos= numNegativos+1
   contador=contador+1
  # Caso 4: número impar y positivo  
  elif num % 2 !=0 and num > 0:
    impares=impares+1
    numPositivos=numPositivos+1
    contador=contador+1
# Finalmente, imprimimos los resultados de los conteos		
print(f"Pares: ", pares)
print(f"impares: ", impares)
print(f"Negativos: ", numNegativos)
print(f"Positivos: " ,numPositivos)



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

# Inicializamos variables
media = 0       # Almacenará la media final
suma = 0        # Acumulará la suma de los números ingresados
contador = 0    # Contará cuántos números válidos se ingresan

# Usamos un bucle for que se ejecuta hasta 100 veces como máximo
for i in range(100):
    # Solicitamos al usuario que ingrese un número
    num1 = int(input("Ingrese un número (0 para detener el programa, máximo 100 números): "))
    # Si el usuario ingresa 0, detenemos el programa
    if num1 == 0:
        break
    # Sumamos el número a la suma total
    suma += num1
    # Incrementamos el contador de números válidos
    contador += 1
    # Calculamos la media actual (parcial)
    media = suma / contador
    # Mostramos la media parcial
    print(f"Media actual: {media}")

# Al finalizar, verificamos si se ingresaron números válidos
if contador > 0:
    # Mostramos la media final
    print(f"\nMedia final de los {contador} números ingresados: {media}")
else:
    # Si no se ingresaron números, informamos al usuario
    print("\nNo se ingresaron números para calcular la media.")
    


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingrese un número para invertir sus dígitos: "))

# Guardamos el número original para mostrarlo al final
numero_original = numero

# Inicializamos la variable que contendrá el número invertido
numero_invertido = 0

# Usamos un bucle while para invertir los dígitos
while numero != 0:
    # Obtenemos el último dígito del número
    digito = numero % 10

    # Agregamos ese dígito al número invertido (desplazándolo a la izquierda)
    numero_invertido = numero_invertido * 10 + digito

    # Eliminamos el último dígito del número original
    numero = numero // 10

# Mostramos el número original e invertido
print(f"Número original: {numero_original}")
print(f"Número invertido: {numero_invertido}")