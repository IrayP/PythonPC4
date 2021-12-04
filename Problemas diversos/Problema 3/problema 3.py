import os

while True:
    try:
        n = int(input("Ingrese un número: "))

        if os.path.isfile("./Problemas diversos/Problema 3/tabla-{}.txt".format(n)):
            m = int(input("Mostrar línea: "))
            ruta = "./Problemas diversos/Problema 3/tabla-{}.txt".format(n)
            archivo = open(ruta,'r')
            with archivo as a:
                lista = archivo.readlines()
                print(lista[m-1])
        else:
            print("No existe tal archivo.")
        break
    except:
        print("No es una entrada válida")
       

