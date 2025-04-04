#Ciclo for
#Especial para recorrer
#Estructuras de datos

#funcion range (python)
#: crea una lista de números en el rango definido por el 
#usuario
numero = int(input("Ingrese un número: "))

for i in range (1, 11):
    resultado = numero * i
    print(numero, "X", i, "=", resultado)