sueldo=int(input("Ingrese el sueldo del empledado:"))
antiguedad=int(input("Ingrese su antiguedad en años:"))
if sueldo<500 and antiguedad>10:
    aumento=sueldo*0.20
    sueldototal=sueldo+aumento
    print("Suelo a pagar")
    print(sueldototal)
else:
    if sueldo<500:
        aumento=sueldo*0.05
        sueldototal=sueldo+aumento
        print("sueldo a pagar")
        print(sueldototal)
    else:
        print("sueldo a pagar")
        print(sueldo)