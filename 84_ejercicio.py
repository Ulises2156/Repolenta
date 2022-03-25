lista=[]
for x in range(5):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print("Lista completa")
print(lista)
print("Mayor lista")
print(mayor)