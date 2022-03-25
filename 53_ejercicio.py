negativos=0
positivos=0
mult15=0
sumapares=0
for f in range(10):
    valor=int(input("Ingese un valor:"))
    if valor<0:
        negativos=negativos+1
    else:
        if valor>0:
            positivos=positivos+1
        if valor%15==0:
            mult15=mult15+1
        if valor%2==0:
            sumapares=sumapares+1
            print("Cantidad de valores negativos:")
            print(negativos)
            print("Cantida de valores positivos:")
            print(positivos)
            print("Cantidad de valores de multiplos de 15:")
            print("La suma de los valores de pares:")
            print(sumapares)
