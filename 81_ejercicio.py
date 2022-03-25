sueldos=[]
suma=0
for x in range(5):
    valor=float(input("Ingrese el sueldo de operario:"))
    sueldos.append(valor)
    suma=suma+valor
print("Lista de sueldos")
print(sueldos)
promedio=suma/5
print("Promedio de sueldos")
print(promedio)