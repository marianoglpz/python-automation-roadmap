import csv
import json
from pathlib import Path


def generate_report():
    # Define file paths using pathlib
    json_path = Path("config.json")
    csv_path = Path("budget_report.csv")

    # 1. Read JSON file
    with open(json_path, "r", encoding="utf-8") as json_file:
        company_data = json.load(json_file)

    # Extract departments list
    departments = company_data.get("departments", [])

    # 2. Write data to CSV file
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write headers
        writer.writerow(["Department", "Employees", "Budget"])

        # Write data rows
        for dept in departments:
            row = [dept["name"], dept["employee"], dept["budget"]]
            writer.writerow(row)

    print(f"Report generated successfully: {csv_path}")


# Execute script
if __name__ == "__main__":
    generate_report()
