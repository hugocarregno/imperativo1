#Realizado por Carreño Hugo
#https://repl.it/@hugocarreno/imperativo1#main.py
#Paradigma Imperativo

#Variables
#1. Crea un variable llamada conejos y asígnale el valor 126.

conejos = 126

#2. Crea una variable llamada zanahorias y asígnale el valor 0.

zanahorias = 0

#3. Muestra el contenido de la variable conejos.

print(conejos)

#4. Modifica el valor de la variable conejos por 150.

conejos = 150

#5. Copia el valor de la variable conejos en la variable zanahorias.

zanahorias = conejos

#6. Imprime el valor de las dos variables con print().

print("conejos vale",conejos,"y zanahorias vale",zanahorias)

#7. Modifica el valor de conejos por 250 y vuelve a mostrar las dos variables.

conejos = 250
print("conejos vale",conejos,"y zanahorias vale",zanahorias)

#Utilizando números
#1. Calcula las siguientes operaciones y muéstralas en pantalla: 3 + 6, 5 – 4, 6 * 3, 8 / 2, 7 / 2

print("3 + 6 =",3+6,",5 – 4 =",5-4,",6 * 3 =",6*3,",8 / 2 =",8/2,",7 / 2 =",7/2)

#2. Escribe las expresiones siguiente en código Python: 1 más 6, 3 multiplicado por 5, 12 menos 8 y 12 dividido entre 4.

1+6,3*5,12-8,12/4

#3. Coloca los paréntesis en su lugar correspondiente para la expresión 4 + 5 * 6 de forma que:
#a. Python realice primero las sumas.

(4 + 5) * 6

#b. Python realice primero las multiplicaciones.

4 + (5 * 6)

#4. Haz un círculo en los número flotantes que ves en la lista: 
#     1 (7.43) (6.0) -12 0 (12.5) 1966 (-6.613) 28

#5. Realiza un círculo en las expresiones que dan como resultado un número flotante (haz el cálculo en Python si lo necesitas):
#   (3 / 5) , (7.3 + 1.4), 6 – 3, 7 + 1, (7 + 1.0), 3 * 8, (7.2 / 3.6), (6 * 9.0), (5.2 – 2.5)

#Cadenas y entradas
#1. Escribe la palabra elefante dentro de una variable llamada animal; Escribe la palabra rosa dentro de una variable llamada color; Crea una variable llamada imagina donde se almacenen las dos variables anteriores: animal y color dando como resultado el valor elefanterosa. En la variable imagina intercala un espacio en blanco para separar las dos palabras.

animal = "elefante"
color = "rosa"
imagina = animal+" "+color

#2. Muestra la pregunta ¿Cuál es tu nombre? y almacénala en la variable nombre. Guarda la primera letra del contenido de la variable nombre dentro de la variable inicial.

nombre = input("¿Cuál es tu nombre?")
inicial = nombre[0]

#3. Dada la variable s= ‘Carlos Gomez Perez’ copia solo el nombre Gomez en una variable llamada m.

s= "Carlos Gomez Perez"
m= s[7:12]

#Ciclos/Bucles
#1. Escribe el código para un bucle tipo for el cual imprime del numero 0 hasta el 7. Utiliza una variable auxiliar llamada n.

for n in range(8):
  print(n)

#2. Modifica el rango del bucle anterior para que ahora imprima del numero 1 hasta el 12.

for n in range(1,13):
  print(n)

#3. Programa un bucle que haga una cuenta regresiva de 10 hasta 1 y por último escriba el mensaje ‘¡Despegue!’:

for n in range(10,0,-1):
  print(n)
print("¡Despegue!")

#Listas
#1. Crea una lista de colores rojo, verde y azul. Lo deberás almacenar en una lista llamada colores.

colores = ["rojo","verde","azul"]

#2. Escribe el código que muestra los colores de la lista que acabas de crear, usando el comando print().

print(colores)

#3. Modifica el código para que ahora solo se muestre el segundo elemento de la lista (verde) que has creado.

print(colores[1])

#4. ¿Cómo cambiarías el primer color rojo por el color rosa en la lista?

colores[0] = "rosa"

#5. Elimina la tercera entrada de la lista.

del colores[2]

#6. Ahora añade el color lila al final de la lista.

colores.append("lila")

#7. Ahora añade el color amarillo en la primera posición (índice 0)

colores.insert(0, "amarillo")

#Verdadero o Falso
#1. Marca con True (Cierto) o False (Falso) estas expresiones donde a = 10; b = 3:
# 1 < 2  T 6 == 6 T 9 != 10 T 8 <= 4       F  4 >= 4       T
# a == 3 F a > 3  T b != 3  F b >= 3       T  b >= 0       T
# a == b F a != b T a < b   F a >= (b + 6) T  a <= (b + 6) F

#2. Escribe en Python las expresiones siguientes:
#a. c es menor que 1000

#c<1000

#b. d no es igual a a

#d != a

#c. d es igual a 6

#d == 6

#d. c es mayor o igual a 12

#c>=12

#e. (c más d) es menor o igual a 10

#(c+d) <= 10

#3. Marca con True (Cierto) o False (Falso) estas expresiones donde a = 10; b = 3. Fíjate que ahora incluímos los operadores lógicos and y or.
#(a == 10 and b == 3) a == 10 and b > 3  a != 10 and b >= 3
#(a >= 5 and b <= 5)  (a > 5 and a < 15) (a == 4 or a == 10)
#(A > 0 or b > 0)     b == a or a < 10   (a > b or b != 100)

#4. Escribe las expresiones booleanas que son ciertas si:
#a y b son menores que 5.

#a<5 and b<5

#a es mayor que 1000 o b es 250.

#a>1000 or b==250

#Bifurcaciones
#1. Completa el código siguiente para que diga “¡Buenos días!” siempre y cuando se introduzca el nombre Ana. 

nombre = input("Introduce tu nombre: ")
if(nombre == "Ana"):
  print("¡Buenos dias!")

#2. Completa el código siguiente para que diga “Coge un pastel” siempre y cuando se introduzca Pastel. De lo contrario haz que le ofrezca una Galleta. 

comida = input("¿Cual es tu comida favorita? ")
if(comida == "Pastel"):
  print("Coge un pastel")
else:
  print("Coge una galleta")

#3. Añade el código necesario al programa anterior para que ofrezca una taza de chocolate sea cual sea la comida favorita.

print("Toma una taza de chocolate")

#4. ¿Qué mostrará en pantalla el programa siguiente?
# For n in range(1000):
#   if n == 3: print(n)

#muestra el número 3

#Bucles del tipo while
#1. Escribe un programa que pregunte por el nombre, hasta que se escriba Carlos.

while(nombre !="Carlos"):
  nombre=input("Ingresar Nombre: ")
print("Hola",nombre)

#Funciones
#1. Define una función llamada agradecimiento que imprima ‘Hola’ seguido del nombre. Cómo harías para ejecutar esta función en Python para decir hola a Ana.

def agradecimiento(nombre):
  print("Hola",nombre)

agradecimiento("Ana")

#2. Una compañía de helados ha creado un código para que se le introduzca el sabor del helado y automáticamente indique el precio:
def precio(sabor):
  if sabor == "chocolate":
    precio = 1.99
  else:
    precio = 2.49 
  return precio
#Respecto al ejercicio anterior, ¿qué se mostrará por pantalla con las siguientes instrucciones?
#a. print(precio(‘banana’)) 

#muestra 2.49

#b. print(precio(‘chocolate’)) 

#muestra 1.99

#c. print(precio(‘vainilla’))

#muestra 2.49