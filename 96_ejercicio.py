lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

# ordenamos de menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print("Lista ordenada de menor a mayor")
print(lista)

# ordenamos de mayor a menor
for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print("Lista ordenada de mayor a menor")
print(lista)
        