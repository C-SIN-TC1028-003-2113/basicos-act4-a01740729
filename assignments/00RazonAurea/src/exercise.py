import math
def main():
    #escribe tu código abajo de esta línea
    pass
    a = float(input('Dame un número: '))
    b = int(input('¿Cuántos decimales? '))

    varphi = (1 + math.sqrt (5)) / 2
    ra = varphi * a

    print("Número: "+str(a))
    print("Decimales a mostrar: "+str(b))
    print("Razón áurea: "+str(round(ra,b)))

if __name__ == '__main__':
    main()