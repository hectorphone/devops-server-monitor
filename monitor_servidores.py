servers = ["web1", "web2", "db1", "db2"]

errores = 0

for server in servers:
    print("Revisando:", server,)

    if server == "db1":
        print("ERROR")
        errores = errores + 1

    else:
        print("OK")

print("Errores totales:", errores)