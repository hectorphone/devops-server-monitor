import os
nombre = input("¿Cómo te llamas?")
edad = int(input("Cuantos años tienes?"))

if edad >= 18:
    print(f"{nombre}, eres mayor de edad")
else:
    print(f"{nombre}, eres menor de edad")

print("----SISTEMA----")
print("Usuario")
os.system("whoami")

print("Ruta actual")
os.system("pwd")

print("Archivos")
os.system("ls")