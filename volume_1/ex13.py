while True:

    user_input = input("Por favor, ingrese su nombre: ").lower().title()

    if not user_input.isalpha():
        print("Debe ingresar un nombre válido")
    elif user_input == "Alejandro":
        print("Bienvenido Alejandro.")
        break
    elif user_input == "Naomi":
        print("Bienvenida Naomi")
        break
    elif user_input == "Sergio":
        print("Bienvenido Sergio")
        break
    else:
        print("Bienvenido invidato/a")
        break
