import math


def grados_a_radianes(grados):
    return grados * (math.pi / 180)


def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)


def main():
    while True:
        try:
            opcion = input(
                "Seleccione la conversión que desea realizar:\n1. De grados a radianes\n2. De radianes a grados\n3. Salir\nIngrese el número de opción: ")

            if opcion == '3':
                print("Saliendo del programa...")
                break

            if opcion not in ['1', '2']:
                print("Opción no válida. Por favor ingrese 1, 2 o 3.")
                continue

            valor = float(input("Ingrese el valor a convertir: "))

            if opcion == '1':
                resultado = grados_a_radianes(valor)
                print(f"{valor} grados sexagesimales equivalen a {resultado:.4f} radianes.")
            else:
                resultado = radianes_a_grados(valor)
                print(f"{valor} radianes equivalen a {resultado:.4f} grados sexagesimales.")

        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")


if __name__ == "__main__":
    main()