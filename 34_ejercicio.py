n=int(input("Cuantos empledados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1
        gastos=gastos+sueldo
        x=x+1
        print("Cantidad de empleados con sueldo entre 100 y 300")
        print(conta1)
        print("Cantidad de empleados con el sueldos mayor a 300")
        print(conta2)
        print("Gastos total de la empresa en sueldos")
        print(gastos)