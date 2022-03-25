"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume.
 Finalizar la carga al ingresar el valor -1
"""
suma=0
valor=int(input("Ingrese valor (-1 finaliza):"))     #se carga el primer valor antes del while
while valor!=-1:
    suma=suma+valor
    valor=int(input("Ingrese  valor (-1 finaliza):"))  #se cargar todos los otros valores dentro del while
    print("La suma de los valores ingresados es")
    print(suma)