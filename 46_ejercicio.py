cantidad=0
n=int(input("Cuantos valores ingresará:"))
for f in range(n):
    valor=int(input("Ingrese el valor:"))
    if valor>=1000:
        cantidad=cantidad+1
print("La cantidad de valores ingresados mayores o iguales a 1000 son")
print(cantidad)