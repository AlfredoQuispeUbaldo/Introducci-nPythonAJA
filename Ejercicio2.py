#Ejercicio2

def obtener_calificacion_numerica():
    calificacion_numerica = -1

    while calificacion_numerica < 0 or calificacion_numerica > 20:
        try:
            calificacion_numerica = int(input("Ingrese la calificación (0-20): "))
            if calificacion_numerica < 0 or calificacion_numerica > 20:
                print("Por favor, ingrese una calificación válida (0-20).")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    return calificacion_numerica


def obtener_calificacion_literal():
    calificacion_numerica = -1
    calificacion_literal = ""

    while calificacion_numerica < 0 or calificacion_numerica > 20:
        try:
            calificacion_numerica = int(input("Ingrese la calificación (0-20): "))
            if calificacion_numerica < 0 or calificacion_numerica > 20:
                print("Por favor, ingrese una calificación válida (0-20).")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    if calificacion_numerica >= 0 and calificacion_numerica <= 10:
        calificacion_literal = "C"
    elif calificacion_numerica >= 11 and calificacion_numerica <= 14:
        calificacion_literal = "B"
    elif calificacion_numerica >= 15 and calificacion_numerica <= 17:
        calificacion_literal = "A"
    elif calificacion_numerica >= 18 and calificacion_numerica <= 20:
        calificacion_literal = "AD"

    return calificacion_literal


def main():
    print("Ingrese la calificación:")
    print("1. En formato numérico (0-20)")
    print("2. En formato literal")

    opcion = 0
    while opcion != 1 and opcion != 2:
        try:
            opcion = int(input("Seleccione una opción (1 o 2): "))
            if opcion != 1 and opcion != 2:
                print("Opción no válida. Por favor seleccione 1 o 2.")
        except ValueError:
            print("Opción no válida. Por favor seleccione 1 o 2.")

    if opcion == 1:
        calificacion_numerica = obtener_calificacion_numerica()
        print("Calificación en formato numérico:", calificacion_numerica)
    elif opcion == 2:
        calificacion_literal = obtener_calificacion_literal()
        print("Calificación en formato literal:", calificacion_literal)


if _name_ == "_main_":
    main()