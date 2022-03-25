print("Datos de la primer persona")
nombre1=input("Ingrese el nombre:")
edad1=int(input("Ingrese la edad:"))
altura1=float(input("Ingrese la altura ej 1.75:"))
print("Datos de la segunda persona")
nombre2=input("Ingrese nombre:")
edad2=int(input("Ingrese la edad:"))
altura2=float(input("Ingrese la altura ej 1.75:"))
print("La pesona mas alta es:")
if altura1>altura2:
    print(altura1)
else:
    print(altura2)