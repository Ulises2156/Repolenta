lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)

#contamos cuantas veces se encuentra el en la lista
cantidad=0
for x in range(5):
    if lista[x]==mayor:
        cantidad=cantidad+1
    if cantidad>1:
        print("El mayor se repite en la lista")