productos=[]
precios=[]
for x in range(5):
    nom=input("Ingrese el nombre del producto:")
    productos.append(nom)
    pre=int(input("Ingrese el precio de dicho producto:"))
    precios.append(pre)

cantidad=0
for x in range(1,5):
    if precios[x]>precios[0]:
        cantidad=cantidad+1

print("Cantidad de productos con un precio mayor al primer producto ingresado")
print(cantidad)
