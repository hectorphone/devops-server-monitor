import os

carpeta = input("Nombre de la carpeta: ")

if os.path.exists(carpeta):
    print("La carpeta ya existe")
else:
    os.mkdir(carpeta)
    print("Carpeta creada")
    
ruta = carpeta + "/log.txt"
print(ruta)

archivo = open(ruta, "w", encoding="utf-8")
archivo.write("Hola\nAdios")
archivo.close()

print("Texto añadido al archivo")