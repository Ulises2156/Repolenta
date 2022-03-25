#con doble comillas
cadena1="juan"
#el resultado es igual con simple comillas
cadena2='ana'
nombre=input("Ingrese su nombre:")
nombre='juan'
print(nombre[0])   #se imprime una j
if nombre[0]=="j": #verificamos si el primer caracter del string es una j
    print(nombre)
    print("comienza con la letra j")