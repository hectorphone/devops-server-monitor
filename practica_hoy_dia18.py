servicio = input("Nombre del servicio: ")
estado = input("¿Está activo? (si/no): ").lower()
    
if estado == "si":
    print(f"El servicio {servicio} está activo")
elif estado == "no":
    print(f"El servicio {servicio} no está activo")
else:
    print("Entrada no valida")

        