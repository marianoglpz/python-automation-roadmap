from pathlib import Path

# 1. Create main test folder
path = Path("Download_Test")
path.mkdir(exist_ok=True)

# 2. Create empty test files
files = ["report.pdf", "picture.jpg", "data.csv", "notes.txt"]
for file in files:
    (path / file).touch()

# 3. Function to organize files
def move_files():
    # Define and create the destination subfolders
    folder_docs = path / "Documents"
    folder_data = path / "Data"
    folder_img = path / "Images"

    folder_docs.mkdir(exist_ok=True)
    folder_data.mkdir(exist_ok=True)
    folder_img.mkdir(exist_ok=True)

    # Iterate through all actual files within the directory
    for file in path.iterdir():
        # Ignore if it is a subfolder instead of a file
        if file.is_dir():
            continue

        # Validate extension and move accordingly
        if file.suffix in [".pdf", ".txt"]:
            file.rename(folder_docs / file.name)
        elif file.suffix == ".csv":
            file.rename(folder_data / file.name)
        elif file.suffix in [".jpg", ".jpeg", ".png"]:
            file.rename(folder_img / file.name)

# Execute the function
move_files()
print("Folders successfully organized!")
