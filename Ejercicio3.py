import math

def grados_a_radianes(grados):
    radianes = (grados * math.pi) / 180
    return radianes

def radianes_a_grados(radianes):
    grados = (radianes * 180) / math.pi
    return grados

def main():
    # Convertir de grados a radianes
    grados = float(input("Ingrese un ángulo en grados sexagesimales: "))
    radianes = grados_a_radianes(grados)
    print("{} grados sexagesimales equivalen a {} radianes.".format(grados, radianes))

    # Convertir de radianes a grados
    radianes = float(input("Ingrese un ángulo en radianes: "))
    grados = radianes_a_grados(radianes)
    print("{} radianes equivalen a {} grados sexagesimales.".format(radianes, grados))

if _name_ == "_main_":
    main()