#variable contadora
#imprimir la tabla de multiplicar del númeor que un usuario 
#ingrese utilizanod un ciclo while
numero= int(input("ingrese un número: "))


i=10

while i>0:
    resultado = numero * i
    print ( numero, "X" , i , "=" , resultado)
#instrcción
##de incremento
    i = i - 1