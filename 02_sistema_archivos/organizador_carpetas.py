from pathlib import Path

# 1. Crear carpeta principal de prueba
path = Path("Descargas_Prueba")
path.mkdir(exist_ok=True)

# 2. Crear archivos vacíos de prueba
nombres = ["reporte.pdf", "foto.jpg", "datos.csv", "notas.txt"]
for nombre in nombres:
    (path / nombre).touch()

# 3. Función para organizar archivos
def mover_archivos():
    # Definir y crear las subcarpetas de destino
    carpeta_docs = path / "Documentos"
    carpeta_datos = path / "Datos"
    carpeta_img = path / "Imagenes"

    carpeta_docs.mkdir(exist_ok=True)
    carpeta_datos.mkdir(exist_ok=True)
    carpeta_img.mkdir(exist_ok=True)

    # Recorrer todos los archivos reales dentro del directorio
    for archivo in path.iterdir():
        # Ignorar si es una subcarpeta en lugar de un archivo
        if archivo.is_dir():
            continue

        # Validar extensión y mover según corresponda
        if archivo.suffix in [".pdf", ".txt"]:
            archivo.rename(carpeta_docs / archivo.name)
        elif archivo.suffix == ".csv":
            archivo.rename(carpeta_datos / archivo.name)
        elif archivo.suffix in [".jpg", ".jpeg", ".png"]:
            archivo.rename(carpeta_img / archivo.name)

# Ejecutar la función
mover_archivos()
print("¡Carpetas organizadas con éxito!")
