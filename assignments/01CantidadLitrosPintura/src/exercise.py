import math
def main():
    #escribe tu código abajo de esta línea
    pass
    a = float(input('Area a pintar en metros: '))
    b = float(input('Rendimiento (m2/l): '))

    l = a / b

    print("Litros a comprar: "+str(math.ceil(l)))

if __name__ == '__main__':
    main()