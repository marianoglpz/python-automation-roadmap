# 📂 Ejercicio 01: Organizador Automático de Carpetas

Script en Python que escanea un directorio local y clasifica archivos en subcarpetas (`Documentos`, `Datos`, `Imagenes`) según su extensión usando `pathlib`.

## 🛠️ Requisitos del Ejercicio
* Crear carpeta de origen `Descargas_Prueba`.
* Crear carpetas de destino automáticamente si no existen.
* Mover `.pdf` y `.txt` a `Documentos`, `.csv` a `Datos`, `.jpg` a `Imagenes`.

## 🧠 Pseudocódigo
1. Importar módulo `pathlib`.
2. Crear directorio principal y subcarpetas con `.mkdir(exist_ok=True)`.
3. Iterar los elementos con `iterdir()`.
4. Evaluar extensión con `.suffix`.
5. Mover archivos con `.rename()`.
