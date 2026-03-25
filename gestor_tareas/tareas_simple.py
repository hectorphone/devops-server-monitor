tarea = input("Escribe una tarea: ")

# Limpiamos espacios
tarea = tarea.strip()

# Comprobamos si está vacía
if tarea == "":
    print("No guardo la tarea")
else:
    with open("tareas_simple.txt", "a") as f:
        f.write(tarea + "\n")
    print("Tarea guardada")

print("\nContenido del archivo:")

with open("tareas_simple.txt", "r") as f:
    contenido = f.readlines()

    for tarea in contenido:
        print(tarea.strip())