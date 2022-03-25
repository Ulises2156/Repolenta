aprobados=0
reprobados=0
for f in range (10):
    nota=int(input("Ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
        print("La cantidad de aprobados es")
        print(aprobados)
        print("Cantidad de reprobados es")
        print(reprobados)

