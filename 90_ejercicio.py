nombres=[]
notas=[]
for x in range(4):
    nom=input("Ingrese nombre del alumno:")
    nombres.append(nom)
    no=int(input("Ingrese la nota del dicho alumno:"))
    notas.append(no)

cantidad=0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x]>=8:
        print("Muy bueno")
        cantidad=cantidad+1
    else:
        if notas[x]>=4:
            print("Bueno")
        else:
            print("Insuficiente")
print("La cantidad de alumnos muy buenos son")
print(cantidad)
