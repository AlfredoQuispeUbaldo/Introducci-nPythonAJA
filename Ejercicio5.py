import turtle

# Función principal
def main():
    longitud_lado = 100  # Longitud de cada lado del cuadrado
    configuracion_inicial()  # Configuración inicial
    dibujar_cuadrado(longitud_lado)  # Dibujar el cuadrado
    turtle.done()  # Mantener la ventana abierta

# Configuración inicial de la tortuga
def configuracion_inicial():
    turtle.speed(1)  # Velocidad de la tortuga
    turtle.penup()   # Levantar el lápiz
    turtle.goto(-50, 50)  # Mover la tortuga al punto inicial
    turtle.pendown()  # Bajar el lápiz

# Función para dibujar un lado del cuadrado
def dibujar_lado(longitud):
    turtle.forward(longitud)
    turtle.right(90)

# Función para dibujar un cuadrado
def dibujar_cuadrado(longitud_lado):
    for _ in range(4):
        dibujar_lado(longitud_lado)

if __name__ == "__main__":
    main()