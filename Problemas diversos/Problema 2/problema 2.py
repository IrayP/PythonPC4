import os

def leer_archivo():
    try:
        n = int(input("Ingrese un número: "))

        if os.path.isfile("./Problemas diversos/Problema 2/tabla-{}.txt".format(n)):
            ruta = "./Problemas diversos/Problema 2/tabla-{}.txt".format(n)
            archivo = open(ruta,'r')   
            with archivo as a:
                data = archivo.read()
                print(data)
        else:
            print("No existe tal archivo.")
    except:
        print("No es una entrada válida")
        return leer_archivo()
    

leer_archivo()
