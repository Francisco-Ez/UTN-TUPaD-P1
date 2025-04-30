#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.

# Se crea una lista de números que comienza en 4, termina en 100 (inclusive), y avanza de 4 en 4
mi_lista= list(range(4,101,4))

# Se imprime la lista generada en la consola
print(mi_lista)




#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

# Se crea una lista que contiene elementos de diferentes tipos de datos
mi_lista= [1,"cadena", "true ", 50, 2.0]

# Se imprime el cuarto elemento de la lista (índice 3), que es el número entero 50
print (mi_lista[3])




#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []

# Se crea una lista vacía sin elementos iniciales
lista_vacia=[]

# Se agrega el elemento "uno" al final de la lista
lista_vacia.append("uno")
# Se agrega el elemento "dos" al final de la lista
lista_vacia.append("dos")
# Se agrega el elemento "tres" al final de la lista
lista_vacia.append("tres")

# Se Imprime el contenido actual de la lista: ['uno', 'dos', 'tres']
print(lista_vacia)



#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

# Se crea una lista llamada 'animales' con cuatro elementos: perro, gato, conejo y pez
animales= ["perro","gato","conejo","pez"]
# Se reemplaza el segundo elemento de la lista (índice 1, que era "gato") por "loro"
animales[1]="loro"
# Se reemplaza el cuarto elemento de la lista (índice 3, que era "pez") por "oso"
animales[3]="oso"
# Se imprime la lista actualizada: ['perro', 'loro', 'conejo', 'oso']
print(animales)




#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#Este programama crea una lista con cinco elementos y luego quita de la lista
#el elemento con el valor más alto. Después muestra la lista nuevamente ya sin ese elemento.




#6)Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

# Se crea la lista
# El resultado será: [10, 15, 20, 25, 30]
mi_lista= list(range(10,31,5))
# Se imprime el primer elemento de la lista (índice 0), que es 10
print(mi_lista[0])
# Se imprime el segundo elemento de la lista (índice 1), que es 15
print(mi_lista[1])




#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.

# Se crea una lista llamada 'autos' que contiene los nombres de algunos modelos de automóviles
# Los elementos de la lista son: ["sedan", "polo", "suran", "gol"]
autos=["sedan","polo","suran","gol"]
# Se cambia el segundo elemento de la lista (índice 1, que era "polo") por "audi"
autos[1]="audi"
# Se cambia el tercer elemento de la lista (índice 2, que era "suran") por "toyota"
autos[2]="toyota"
# Se imprime la lista actualizada, que ahora contiene: ['sedan', 'audi', 'toyota', 'gol']
print(autos)




#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

# Se crea una lista vacía llamada 'dobles'
dobles=[]
# Se agrega el número 10 al final de la lista 'dobles' usando el método append()
dobles.append(10)
# Se agrega el número 20 al final de la lista 'dobles'
dobles.append(20)
# Se agrega el número 30 al final de la lista 'dobles'
dobles.append(30)

# Se imprime el contenido actual de la lista 'dobles'
# En este caso, la lista será: [10, 20, 30]
print(dobles)




#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# Se asigna la lista de compras del Cliente 3 a la variable 'cliente3'
cliente3= compras[2]
# Se agrega "jugo" a la lista de compras de Cliente 3 (al final de la lista)
cliente3.append("jugo")
# Se asigna la lista de compras del Cliente 2 a la variable 'cliente2'
cliente2=compras[1]
# Se cambia el segundo elemento de la lista de compras de Cliente 2 (índice 1)
# "fideos" se reemplaza por "tallarines"
cliente2[1]="tallarines"
# Se asigna la lista de compras del Cliente 1 a la variable 'cliente1'
cliente1=compras[0]
# Se elimina "pan" de la lista de compras de Cliente 1
cliente1.remove("pan")

# Se imprime la lista de compras actualizada para todos los clientes
# El resultado será: 
# [['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]
print(compras)




#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

#Se crea la lista
lista_anidada = [15,True,[25.5, 57.9, 30.6],False]

# Se imprime el contenido de la lista 'lista_anidada'
# La salida será: [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
