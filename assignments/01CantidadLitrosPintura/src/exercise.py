import math
def main():
    #escribe tu código abajo de esta línea
    pass
    a = float(input('Introduce el area a pintar en metros: '))
    b = float(input('¿Cuantos metros puede pintar cada litro? '))

    l = a / b

    print("NArea a pintar en metros: "+str(a))
    print("Rendimiento (m2/l): "+str(b))
    print("Litros a comprar: "+str(math.ceil(l)))

if __name__ == '__main__':
    main()