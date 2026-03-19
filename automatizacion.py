import os

carpeta = input("Nombre de la carpeta: ")

if os.path.exists(carpeta):
    print("Carpeta ya existe")
else:
    os.mkdir(carpeta)
    print("Carpeta creada")