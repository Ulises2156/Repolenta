totalpreguntas=int(input("Ingrese la cantidad total de preguntas del examen:"))
totalcorrectas=int(input("Ingrese la cantidad total e preguntas contestada correctamente:"))
porcentaje=totalcorrectas*100/ totalpreguntas
if porcentaje >=90:
    print("Nivel máximo")
else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
                print("Fuera de nivel")