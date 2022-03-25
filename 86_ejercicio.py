from tkinter import N


nombres=[]
for x in range(5):
    nom=input("Ingrese nombre de pesonas:")
    nombres.append(nom)

nombremenor=nombres[0]
for x in range(1,5):
    if nombres[x]<nombremenor:
        nombremenor=nombres[x]
print("La lista completa de nombres ingresados son")
print(nombres)
print("El nombre menor en orden alfabetico es:")
print(nombremenor)