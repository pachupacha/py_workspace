while True:
    nombre = input("Ingrese su nombre: ").title()
    if not nombre.isalpha():
        print("Ingrese un nombre válido.")
    else: 
        break

while True:
    while True:
        edad = input("Ingrese su edad: ")
        if not edad.isdigit() or '.' in edad or int(edad) > 100:
            print("Ingrese una edad válida.")
        else:
            break
    if int(edad) < 17 or int(edad) > 21:
        print("No cumple los requisitos de edad para acceder a la beca.")
        break
    break

if int(edad) >= 17 and int(edad) <= 21:
    while True:
        while True:
            nota_cuatrimestre_1 = float(input("Ingrese la nota final del primer cuatrimestre: "))
            if nota_cuatrimestre_1 < 0 or nota_cuatrimestre_1 > 10.0:
                print("Ingrese una nota válida")
            else:
                break

        while True:
            nota_cuatrimestre_2 = float(input("Ingrese la nota final del segundo cuatrimestre: "))
            if nota_cuatrimestre_2 < 0 or nota_cuatrimestre_2 > 10.0:
                print("Ingrese una nota válida")
            else:
                break

        while True:
            nota_cuatrimestre_3 = float(input("Ingrese la nota final del tercer cuatrimestre: "))
            if nota_cuatrimestre_3 < 0 or nota_cuatrimestre_3 > 10.0:
                print("Ingrese una nota válida")
            else:
                break

        nota_final = (nota_cuatrimestre_1 + nota_cuatrimestre_2 + nota_cuatrimestre_3) / 3

        if nota_final <= 8:
            print(f"Promedio nota final: {nota_final}")
            print("No cumple los requisitos académicos para acceder a la beca.")
        else:
            print(f"Promedio nota final: {nota_final}")
            print(f"Enhorabuena {nombre}, usted cumple con todos los requisitos para acceder a la beca")
        break
