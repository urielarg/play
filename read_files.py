import os

lista_archivos = os.listdir("/home/ian/Documentos/proyectos/textfiles/files/")
a = 1
directorio = '/home/ian/Documentos/proyectos/textfiles/files/'

for archivo in lista_archivos:
    os.chdir(directorio)
    archivo_abierto = open(archivo,"a")
    archivo_abierto.write("Esta linea es agregada automaticamente, estas viendo el archivo numero " + str(a))
    archivo_abierto.close()
    nuevo_nombre = 'newname' + str(a) + '.txt'
    os.rename(directorio + archivo, directorio + nuevo_nombre)
    a += 1

