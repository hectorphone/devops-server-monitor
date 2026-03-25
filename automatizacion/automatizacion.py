import os

carpeta = input("Nombre de la carpeta: ")
texto = input("Escribe el texto: ")

if os.path.exists(carpeta):
    print("La carpeta ya existe")
else:
    os.mkdir(carpeta)
    print("Carpeta creada")
    
ruta = os.path.join(carpeta, "log.txt")
print(ruta)

archivo = open(ruta, "a", encoding="utf-8")
archivo.write("\n[LOG] " + texto)
archivo.close()

print("Texto añadido al archivo")