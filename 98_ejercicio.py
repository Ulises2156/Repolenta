paises=[]
habitantes=[]
for x in range(5):
    nom=input("Ingrese el nombre del pais:")
    paises.append(nom)
    cant=int(input("Cantidad de habitantes"))
    habitantes.append(cant)

# ordenamiento alfabetico
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print("Listado de paises en orden alfabetico")
for x in range(5):
     print(paises[x],habitantes[x])

# ordenamiento por cantidad de habitantes
for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print("Listado de paises por cantidad de habitantes")
for x in range(5):
     print(paises[x],habitantes[x])
