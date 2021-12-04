import os


while True:
    try:
        n = int(input("Ingrese un número: "))
        ruta = "./Problemas diversos/Problema 1/tabla-{}.txt".format(n)
        archivo = open(ruta,'w')
        with archivo as a:
            for i in range(1,13):
                cadena = "{} x {} = {}\n".format(n,i,n*i)
                archivo.write(cadena)
        break
    except:
        print("No es una entrada válida")
        