# DevOps Server Monitor

Proyecto de prácticas en Python orientado a automatización básica y organización de scripts.

## Estructura del proyecto

- `automatizacion/`: contiene el script `automatizacion.py` y la carpeta `prueba/`.
- `monitor_servidores/`: contiene el script `monitor_servidores.py`.
- `README.md`: documentación básica del proyecto.

## Descripción

### automatizacion
Script en Python que permite:
- pedir al usuario el nombre de una carpeta,
- pedir un texto,
- crear la carpeta si no existe,
- guardar el texto en un archivo `log.txt`,
- añadir entradas con formato `[LOG]`.

### monitor_servidores
Script en Python orientado a realizar comprobaciones básicas sobre servidores.

## Uso

### Ejecutar el script de automatización
```bash
cd automatizacion
python automatizacion.py