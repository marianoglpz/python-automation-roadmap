# 📂 Exercise 01: Automatic Folder Organizer

A Python script that scans a local directory and sorts files into subfolders (`Documents`, `Data`, `Images`) based on their extension using `pathlib`.

## 🛠️ Exercise Requirements
* Create a source folder named `Descargas_Prueba`.
* Automatically create destination folders if they do not exist.
* Move `.pdf` and `.txt` files to `Documents`, `.csv` to `Data`, and `.jpg` to `Images`.

## 🧠 Pseudocode
1. Import the `pathlib` module.
2. Create the main directory and subfolders using `.mkdir(exist_ok=True)`.
3. Iterate through items using `iterdir()`.
4. Check the file extension using `.suffix`.
5. Move files using `.rename()`.
