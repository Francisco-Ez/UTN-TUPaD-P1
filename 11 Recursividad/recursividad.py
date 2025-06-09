#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario:


# Función recursiva que calcula el factorial de un número
def funcion_recur(num):
    # Caso base: el factorial de 0 es 1 por definición
    if num == 0:
        return 1
    else:
        # Paso recursivo: n! = n * (n-1)!
        return num * funcion_recur(num - 1)

#Main: Bloque principal del programa

# Solicita al usuario que ingrese un número entero
numero = int(input("Escriba un número para mostrar su factorial: "))

# Calcula e imprime el factorial del número ingresado
print(f"El factorial de {numero} es {funcion_recur(numero)}")

# Imprime los factoriales de todos los números desde 1 hasta (numero - 1)
print(f"El factorial de todos los números enteros entre 1 y {numero} es:")
for i in range(1, numero):
    # Calcula e imprime el factorial de cada número en el rango
    print(f"Factorial de {i} = {funcion_recur(i)}")




#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.


# Función recursiva para calcular el valor de Fibonacci en una posición dada
def fibonacci(num):
    # Caso base: si la posición es 0, el valor es 0
    if num == 0:
        return 0
    # Caso base: si la posición es 1, el valor es 1
    elif num == 1:
        return 1
    else:
        # Llamada recursiva: suma de los dos valores anteriores en la serie
        return fibonacci(num - 1) + fibonacci(num - 2)

#Main: Bloque principal del programa

# Solicita al usuario un número entero para determinar hasta qué posición calcular la serie de Fibonacci
num = int(input("Escribe un número para obtener la serie Fibonacci hasta esa posición: "))

# Llama a la función fibonacci con el número ingresado (aunque el resultado no se usa directamente)
fibonacci(num)

# Imprime la serie de Fibonacci desde la posición 0 hasta la posición n-1
for i in range(num):
    print(fibonacci(i), end=" ")




#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente. Prueba esta función en un algoritmo general. 


# Función recursiva para calcular la potencia de un número
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es igual a 1
    if exponente == 0:
        return 1
    else:
        # Caso recursivo: multiplicamos la base por el resultado de la potencia con el exponente reducido en 1
        return base * potencia(base, exponente - 1)

# Main: Bloque principal del programa

# Solicita al usuario ingresar el número base para calcular la potencia
base = int(input("Escriba un número base para calcular su potencia: "))

# Solicita al usuario ingresar el exponente al que desea elevar la base
exponente = int(input("Escriba el exponente: "))

# Llama a la función potencia para calcular el resultado de elevar la base al exponente
resultado = potencia(base, exponente)

# Muestra el resultado en un formato legible
print(f"{base} elevado a {exponente} es {resultado}")




#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.


# Función recursiva para convertir un número decimal a binario
def conversion_binaria(numero):
    # Caso base: si el número es menor que 2 (es 0 o 1), simplemente lo devolvemos como una cadena
    if numero < 2:
        return str(numero)
    else:
        # Caso recursivo: dividimos el número entre 2 y concatenamos el residuo de esa división
        # Esto genera los bits del número en orden inverso, por lo que la recursión ayuda a formar
        # el número binario desde el bit más significativo al menos significativo.
        return conversion_binaria(numero // 2) + str(numero % 2)

# Main: Bloque principal del programa

# Solicita al usuario un número entero en formato decimal para convertirlo a binario
numero_decimal = int(input("Escriba un número para pasarlo a binario: "))

# Llama a la función conversion_binaria y muestra el resultado de la conversión a binario
print(conversion_binaria(numero_decimal))



#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.


# Función recursiva para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    # Caso base 1: Si la longitud de la palabra es 1 o menos, es un palíndromo por definición
    if len(palabra) <= 1:
        return True
    
    # Caso base 2: Si el primer y último carácter no son iguales, no es un palíndromo
    if palabra[0] != palabra[-1]:
        return False
    
    # Caso recursivo: Llamada recursiva eliminando el primer y último carácter de la palabra
    # Se sigue verificando si el resto de la palabra (sin el primer y último carácter) es un palíndromo
    return es_palindromo(palabra[1:-1])




#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.


# Función recursiva para calcular la suma de los dígitos de un número
def suma_digitos(n):
    # Caso base: Si el número es 0, la suma de sus dígitos es 0
    if n == 0:
        return 0
    
    # Caso recursivo: Se obtiene el último dígito (n % 10) y se suma al resultado de la llamada recursiva
    # El número n se divide por 10 (n // 10) para eliminar el último dígito y sumar los dígitos restantes
    return n % 10 + suma_digitos(n // 10)


# Main: Bloque principal del programa

# Solicita al usuario ingresar un número entero positivo
num = int(input("Escriba un número entero positivo para calcular la suma de sus dígitos: "))

# Llama a la función suma_digitos y muestra el resultado con el número ingresado
print(f"La suma de todos los dígitos en {num} es {suma_digitos(num)}")




#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.


# Función recursiva para contar el total de bloques necesarios para construir una pirámide
def contar_bloques(n):
    # Caso base: Si solo queda un bloque (nivel 1), se devuelve 1
    if n == 1:
        return 1
    
    # Caso recursivo: El total de bloques en el nivel n es la suma de los bloques en el nivel n 
    # más los bloques necesarios para los niveles anteriores (contados recursivamente)
    return n + contar_bloques(n - 1)


# Main: Bloque principal del programa

# Solicita al usuario que ingrese la cantidad de bloques en el nivel más bajo de la pirámide
num = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

# Validación para asegurarse de que el número de bloques es mayor o igual a 1
if num < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    # Llama a la función contar_bloques con el número ingresado y muestra el resultado total
    print(f"Se necesitan {contar_bloques(num)} bloques en total para construir la pirámide.")



#8)Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

# Función recursiva para contar cuántas veces aparece un dígito específico en un número
def contar_digito(numero, digito):
    # Caso base: Si el número es 0, hemos revisado todos los dígitos, por lo que devolvemos 0
    if numero == 0:
        return 0
    
    # Extraer el último dígito del número utilizando la operación módulo (n % 10)
    ultimo = numero % 10
    
    # Si el último dígito coincide con el dígito buscado, contamos una aparición
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)  # Llamada recursiva para el resto del número
    
    # Si el último dígito no es igual al dígito buscado, simplemente continuamos con el resto del número
    else:
        return contar_digito(numero // 10, digito)

# Solicitar al usuario un número entero positivo para analizar
numero = int(input("Ingresá un número entero positivo: "))

# Solicitar al usuario el dígito que desea contar en el número
digito = int(input("Ingresá un dígito (0-9): "))

# Llamada a la función contar_digito y almacenar el resultado
resultado = contar_digito(numero, digito)

# Mostrar el resultado: cuántas veces aparece el dígito en el número
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")