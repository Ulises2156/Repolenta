lista1=[]
print("Carga de la primera lista")
for x in range(4):
    valor=int(input("Ingrese el valor:"))
    lista1.append(valor)

lista2=[]
print("Carga de la segunda lista")
for x in range(4):
    valor=int(input("Ingrese valor:"))
    lista2.append(valor)

listasuma=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    listasuma.append(suma)
print("Lista resultante:")
print(listasuma)