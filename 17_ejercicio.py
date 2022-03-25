num=int(input("Ingrese un valor de hasta tres digitos positivos:"))
if num<10:
    print("Tiene un digito")
else:
    if num<100:
        print("Tiene dos digitos")
    else:
        if num<1000:
            print("Tiene tres digitos")
        else:
            print("Error en la entrada de datos.")
