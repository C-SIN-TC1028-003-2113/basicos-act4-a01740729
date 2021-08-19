import math
def main():
    #escribe tu código abajo de esta línea
    pass
    a = float(input('Número: '))
    b = int(input('Decimales a mostrar: '))

    varphi = (1 + math.sqrt (5)) / 2
    ra = varphi * a

    print("Razón áurea: "+str(round(ra,b)))

if __name__ == '__main__':
    main()