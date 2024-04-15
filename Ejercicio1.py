#Ejercicio1 - Hecho por Alfredo - Jhonn - Anyulieth

def calcular_intereses(capital, tasa, años):
    tasa_decimal = tasa / 100
    monto_total = capital * (1 + tasa_decimal)**años
    intereses_generados = monto_total - capital
    return intereses_generados

# Leer los datos de entrada

while True:
        try:
            capital_inicial = float(input("Ingrese el capital inicial: "))
            tasa_interes = float(input("Ingrese la tasa de interés (%): "))
            años = int(input("Ingrese el número de años: "))

            if capital_inicial.is_integer() or tasa_interes.is_integer() or años.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un numero valido.")
        except ValueError:
            print("Por favor, ingrese un número válido")

# Calcular los intereses
intereses = calcular_intereses(capital_inicial, tasa_interes, años)

# Imprimir los resultados
print("Intereses generados en", años, "años:", intereses)