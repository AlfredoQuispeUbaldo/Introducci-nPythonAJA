def calcular_raiz_cuadrada(numero, tolerancia=0.0001):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")

    if numero == 0:
        return 0

    x = numero / 2  # Aproximación inicial

    while True:
        raiz_aproximada = 0.5 * (x + numero / x)
        if abs(raiz_aproximada - x) < tolerancia:
            break
        x = raiz_aproximada

    return raiz_aproximada

def main():
    while True:
        try:
            numero = float(input("Ingrese un número para calcular su raíz cuadrada (o ingrese '0' para salir): "))
            if numero == 0:
                print("Saliendo del programa...")
                break
            raiz_cuadrada = calcular_raiz_cuadrada(numero)
            print(f"La raíz cuadrada de {numero} es aproximadamente {raiz_cuadrada:.4f}")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()