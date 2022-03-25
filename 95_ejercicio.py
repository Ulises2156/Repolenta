cantidad=int(input("Cuantos empleados tiene la empresa?"))
sueldos=[]
for x in range(cantidad):
    su=int(input("Ingrese sueldo:"))
    sueldos.append(su)

# ordenamos la lista
for k in range(cantidad-1):
    for x in range(cantidad-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista de sueldos ordenados")
print(sueldos)
