#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios 
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#1): Añadir nuevas frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


#2): Actualizar los precios de las frutas indicadas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


#3): Crear una lista con solo los nombres de las frutas
frutas = list(precios_frutas.keys())

# Mostrar el diccionario actualizado y la lista de frutas
print("Diccionario actualizado de precios:")
print(precios_frutas)  # Imprime el diccionario con los precios actuales de las frutas

print("\nLista de frutas:")
print(frutas) # Imprime la lista de frutas (solo nombres)




#4)Escribí un programa que permita almacenar y consultar números telefónicos.

# Inicializamos un diccionario vacío llamado 'contactos' para almacenar los nombres y números de teléfono
contactos={}

# Pedimos al usuario que ingrese 5 contactos
# Usamos un bucle 'for' que se repite 5 veces para pedir 5 nombres y 5 números.
for i in range(5):
    print(f"\n--- Contacto número {i+1} ---") # Imprimimos un mensaje indicando el número del contacto
    # Pedimos el nombre del contacto
    nombre_contacto = input("Escribe el nombre de la persona: ")

    # Pedimos el número de teléfono del contacto
    numero_telefono = input(f"Ahora escribe el número de teléfono de {nombre_contacto}: ")

    # Guardamos el nombre y el número en nuestro diccionario 'contactos'
    contactos[nombre_contacto] = numero_telefono
    print(f"¡Listo! Se guardó a {nombre_contacto}.") # Confirmamos que el contacto se guardó correctamente

# Buscamos un contacto en el diccionario
print("\n--- ¡Momento de buscar un contacto! ---")
while True: # Este bucle hará que podamos buscar contactos una y otra vez hasta que el usuario decida salir
    # Pedimos al usuario que ingrese un nombre para buscar en los contactos
    nombre_a_buscar = input("¿Qué nombre quieres buscar? (Escribe 'fin' para salir): ")

    # Si el usuario escribe 'fin', salimos del bucle y terminamos el programa
    if nombre_a_buscar == 'fin':
        print("Gracias por usar el programa.") # Mensaje de despedida
        break # Detenemos el bucle y terminamos la ejecución del programa

    # Verificamos si el nombre ingresado por el usuario existe en el diccionario 'contactos
    if nombre_a_buscar in contactos:
        # Si el nombre existe en el diccionario, mostramos el número de teléfono asociado
        print(f"El número de {nombre_a_buscar} es: {contactos[nombre_a_buscar]}")
    else:
        # Si el nombre no se encuentra, le avisamos al usuario
        print(f"Lo siento, no encontré a {nombre_a_buscar} en tus contactos.")




#5)Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra


# Función que analiza una frase ingresada por el usuario, 
# mostrando las palabras únicas y el recuento de ocurrencias de cada palabra.
def analizar_frase():
    # Solicitar al usuario que ingrese una frase
    frase = input("Ingresa una frase: ")
    
    # Dividir la frase en palabras y convertirlas a minúsculas para un conteo preciso
    palabras = frase.lower().split()
    
    # Obtener palabras únicas usando un set
    palabras_unicas = set(palabras)
    
    # Contar cuántas veces aparece cada palabra usando un diccionario
    recuento_palabras = {}
    for palabra in palabras:
        # Si la palabra ya existe en el diccionario, se incrementa su contador.
        # Si no, se agrega con un contador inicial de 1.
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
        
    # Imprimir las palabras únicas
    print(f"Palabras únicas: {palabras_unicas}")
    # Imprimir el recuento de las palabras
    print(f"Recuento: {recuento_palabras}")

# Llamar a la función para ejecutar el programa
analizar_frase()




#6)Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

# Función que solicita las notas de 3 alumnos y calcula su promedio.
def calcular_promedios_principiante():
    # Creamos un diccionario vacío llamado 'alumnos' que almacenará los nombres de los alumnos 
    # y sus respectivas notas como una tupla (nota1, nota2, nota3).
    alumnos = {} 

    # Usamos un bucle 'for' para pedir los datos de 3 alumnos
    for i in range(3):
        # Pedimos el nombre del alumno al usuario.
        nombre_alumno = input(f"¿Cómo se llama el alumno número {i+1}? ")
        
        # Pedimos las 3 notas del alumno, asegurándonos de que las ingrese separadas por comas.
        notas_texto = input(f"Escribe las 3 notas de {nombre_alumno} separadas por comas (por ejemplo: 7,8,9): ")
        
        # Separamos el texto de las notas usando la coma como delimitador
        lista_notas_texto = notas_texto.split(',')
        
        # Convertimos las notas de texto (string) a números enteros (int)
        nota1 = int(lista_notas_texto[0]) # La primera nota
        nota2 = int(lista_notas_texto[1]) # La segunda nota
        nota3 = int(lista_notas_texto[2]) # La tercera nota
        
        # Creamos una tupla con las 3 notas
        notas_del_alumno = (nota1, nota2, nota3)
        
        # Guardamos el nombre del alumno como clave y sus notas como valor en el diccionario 'alumnos'
        alumnos[nombre_alumno] = notas_del_alumno

    # Imprimimos el encabezado para los promedios
    print("\n--- ¡Aquí están los promedios! ---")
    
    # Recorremos el diccionario 'alumnos', donde 'nombre' es el nombre del alumno
    # y 'notas' es la tupla con sus 3 notas.
    for nombre, notas in alumnos.items():
        # Sumamos las 3 notas del alumno
        suma_notas = notas[0] + notas[1] + notas[2]
        
        # Calculamos el promedio dividiendo la suma de las notas entre 3 (la cantidad de notas)
        promedio = suma_notas / 3
        
        # Imprimimos el nombre del alumno y su promedio con dos decimales
        print(f"El promedio de {nombre} es: {promedio:.2f}")

# Llamamos a la función para ejecutar el programa
calcular_promedios_principiante()




#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Se definen los conjuntos (sets) de estudiantes que aprobaron cada parcial
# Los números representan identificadores únicos de los estudiantes
parcial_1 = {1, 2, 3, 4, 5} # Estudiantes que aprobaron el primer parcial
parcial_2 = {4, 5, 6, 7, 8} # Estudiantes que aprobaron el segundo parcial

# Usamos la intersección (&) para encontrar los estudiantes que aprobaron ambos parciales
aprobados_ambos= parcial_1 & parcial_2
print(f"Aprobaron ambos parciales: {aprobados_ambos}")

# Usamos la diferencia simétrica (^) para obtener los que aprobaron solo uno de los dos parciales
# Es decir, aquellos que están en uno de los dos sets pero no en ambos
aprobados_solo_uno = parcial_1 ^ parcial_2
print(f"Aprobaron solo uno de los dos parciales: {aprobados_solo_uno}")


# Usamos la unión (|) para combinar todos los estudiantes que aprobaron al menos un parcial
# Esto incluye a los que aprobaron uno o ambos parciales
aprobados_total = parcial_1 | parcial_2
print(f"Estudiantes que aprobaron al menos un parcial: {aprobados_total}")




#8)Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock
productos = {
    "manzana": 50,
    "banana": 30,
    "naranja": 40,
    "pera": 20
}

# Función para consultar el stock de un producto
def consultar_stock(producto):
    # Verificamos si el producto está en el diccionario 'productos'
    if producto in productos:
        # Si el producto existe, mostramos su cantidad en stock
        print(f"El stock de {producto} es: {productos[producto]} unidades.")
    else:
        # Si el producto no está, informamos que no está en el stock
        print(f"El producto {producto} no está en el stock.")

# Función para agregar unidades al stock de un producto
def agregar_unidades(producto, cantidad):
    # Verificamos si el producto ya existe en el diccionario
    if producto in productos:
        # Si el producto existe, incrementamos su stock por la cantidad ingresada
        productos[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de {producto}. Nuevo stock: {productos[producto]}")
    else:
        # Si el producto no existe en el diccionario, informamos al usuario
        print(f"El producto {producto} no está en el stock.")

# Función para agregar un nuevo producto al stock
def agregar_producto(producto, cantidad):
    # Verificamos si el producto ya existe en el diccionario
    if producto in productos:
        # Si el producto ya existe, informamos que no es necesario agregarlo
        print(f"El producto {producto} ya está en el stock.")
    else:
        # Si el producto no existe, lo agregamos con la cantidad especificada
        productos[producto] = cantidad
        print(f"El producto {producto} ha sido agregado con {cantidad} unidades.")

# Menú interactivo para permitir al usuario seleccionar una opción
while True:
    # Mostramos las opciones disponibles para el usuario
    print("\n----- Menú -----")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    # Leemos la opción elegida por el usuario
    opcion = input("Elige una opción (1-4): ")

    # Opción 1: Consultar el stock de un producto
    if opcion == "1":
        # Pedimos el nombre del producto
        producto = input("Ingresa el nombre del producto: ").lower()
        consultar_stock(producto)

    # Opción 2: Agregar unidades al stock de un producto existente
    elif opcion == "2":
        # Pedimos el nombre del producto y la cantidad de unidades a agregar
        producto = input("Ingresa el nombre del producto: ").lower()
        cantidad = int(input("Ingresa la cantidad de unidades a agregar: "))
        agregar_unidades(producto, cantidad)
    
    # Opción 3: Agregar un nuevo producto al stock
    elif opcion == "3":
        # Pedimos el nombre y la cantidad del nuevo producto
        producto = input("Ingresa el nombre del nuevo producto: ").lower()
        cantidad = int(input("Ingresa la cantidad de unidades: "))
        agregar_producto(producto, cantidad)
    
    # Opción 4: Salir del programa
    elif opcion == "4":
        print("¡Hasta luego!") # Mensaje de despedida
        break # Salimos del bucle y terminamos el programa
    
    # Si el usuario ingresa una opción no válida, mostramos un mensaje de error
    else:
        print("Opción no válida. Por favor elige una opción entre 1 y 4.")



 
 #9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

 # Diccionario que representa la agenda, donde las claves son tuplas (día, hora) y los valores son eventos
agenda = {
    ("lunes", "10:00"): "Reunión",    # Evento en lunes a las 10:00
    ("martes", "15:00"): "Clase de inglés"  # Evento en martes a las 15:00
}

# Función para consultar un evento en la agenda dado un día y una hora
def consultar_evento(dia, hora):
    # Creamos una tupla que represente la clave en el diccionario
    clave = (dia, hora)

    # Verificamos si la clave existe en el diccionario de la agenda
    if clave in agenda:
        # Si el evento existe, mostramos el evento programado
        print(f"El evento para {dia} a las {hora} es: {agenda[clave]}")
    else:
        # Si el evento no existe, mostramos un mensaje indicándolo
        print(f"No hay ningún evento programado para {dia} a las {hora}.")

# Función para agregar un nuevo evento a la agenda
def agregar_evento(dia, hora, evento):
    # Creamos una tupla que represente la clave en el diccionario
    clave = (dia, hora)

    # Verificamos si ya existe un evento para ese día y hora
    if clave in agenda:
        # Si ya existe un evento, informamos que no se puede agregar uno nuevo
        print(f"Ya existe un evento programado para {dia} a las {hora}.")
    else:
        # Si no existe, agregamos el nuevo evento a la agenda
        agenda[clave] = evento
        print(f"Evento '{evento}' agregado para {dia} a las {hora}.")

# Función para listar todos los eventos programados en la agenda
def listar_eventos():
    # Verificamos si la agenda tiene eventos programados
    if agenda:
        # Si hay eventos, mostramos todos los eventos en la agenda
        print("\nAgenda completa:")
        for (dia, hora), evento in agenda.items():
            # Imprimimos cada evento con su día y hora
            print(f"{dia} a las {hora}: {evento}")

    else:
        # Si no hay eventos, informamos que la agenda está vacía
        print("La agenda está vacía.")


# Menú interactivo donde el usuario puede elegir qué acción realizar
while True:
    # Mostramos las opciones disponibles en el menú
    print("\n----- Menú -----")
    print("1. Consultar un evento")
    print("2. Agregar un evento")
    print("3. Listar todos los eventos")
    print("4. Salir")

    # Leemos la opción elegida por el usuario
    opcion = input("Elige una opción (1-4): ")
   
    # Opción 1: Consultar un evento
    if opcion == "1":
        # Pedimos al usuario que ingrese el día y la hora del evento a consultar
        dia = input("Ingresa el día: ").lower()
        hora = input("Ingresa la hora (formato 24h, ej. 10:00): ")
        consultar_evento(dia, hora)
    
    # Opción 2: Agregar un nuevo evento
    elif opcion == "2":
        # Pedimos el día, la hora y el nombre del evento
        dia = input("Ingresa el día: ").lower()
        hora = input("Ingresa la hora (formato 24h, ej. 10:00): ")
        evento = input("Ingresa el nombre del evento: ")
        agregar_evento(dia, hora, evento)
    
    # Opción 3: Listar todos los eventos
    elif opcion == "3":
        listar_eventos()
    
    # Opción 4: Salir del programa
    elif opcion == "4":
        print("¡Hasta luego!") # Mensaje de despedida
        break # Salimos del bucle y terminamos el programa
    
    # Si el usuario ingresa una opción no válida, mostramos un mensaje de error
    else:
        print("Opción no válida. Por favor elige una opción entre 1 y 4.")




#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

# Diccionario original que relaciona países con sus capitales
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "México": "Ciudad de México",
    "Francia": "París"}

# Creamos un nuevo diccionario vacío donde se invertirán las claves y valores
invertido = {}

# Recorremos cada par (clave: país, valor: capital) del diccionario original
for pais, capital in original.items():
    # En el nuevo diccionario, usamos la capital como clave y el país como valor
    invertido[capital] = pais


# Mostramos el diccionario invertido, donde ahora las capitales son claves y los países los valores
print(invertido)
