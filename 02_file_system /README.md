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

---

# 📊 Exercise 02: Report Generator from JSON Configuration

A Python script that reads system configuration data from a JSON file and processes it into a structured CSV budget report.

## 🛠️ Exercise Requirements
* Create a JSON file (`config.json`) containing company information and department budget data.
* Implement a function `generate_report()` that reads and parses `config.json` using `json.load()`.
* Extract the list of departments and export them into a CSV file (`budget_report.csv`).
* Include CSV headers (`department`, `employees`, `budget`) and format rows appropriately.

## 🧠 Pseudocode
1. Import `json` and `csv` modules.
2. Define function `generate_report()`:
   - Open and read `config.json` using `json.load()`.
   - Store the `"departments"` list from the loaded dictionary.
   - Open `budget_report.csv` in write mode (`'w'`) with `newline=""`.
   - Initialize `csv.writer` and write header row: `["Department", "Employees", "Budget"]`.
   - Iterate through each department entry:
     - Extract name, employee count, and budget.
     - Write extracted data row to CSV.
3. Call `generate_report()` and display a success message.
