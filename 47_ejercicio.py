n=int(input("Cuantos triángulos preocesará:"))
cantidad=0
for x in range(n):
    base=int(input("Ingrese el valor de base:"))
    altura=int(input("Ingrese el valor de la altura:"))
    superficie=base*altura/2
    print("La superficie es")
    if superficie>12:
        cantidad=cantidad+1
        print("La cantidad de triángulos con superficie a 12 son")
        print(cantidad)