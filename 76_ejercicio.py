lista=[1000, 6000, 400, 23, 130,400,60, 2000]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1
print("La lista esta constituida  por los elementos:")
print(lista)
print("La cantidad de valores mayores a 100 en la lista son:")
print(cantidad)