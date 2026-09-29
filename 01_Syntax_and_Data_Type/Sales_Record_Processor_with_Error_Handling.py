# Sales Record Processor with Error Handling


	# Lista + diccionarios
registros_ventas = [
    {"id": 101, "producto": "Laptop", "monto": "1200.50"},
    {"id": 102, "producto": "Mouse", "monto": "25.00"},
    {"id": 103, "producto": "Teclado", "monto": "N/A"},
    {"id": 104, "producto": "Monitor", "monto": "300.00"},
    {"id": 105, "producto": "Silla Gamer", "monto": None}
]


def process_sales(registros):

    total_amount = 0
    successful_records = 0

    for sale in registros: # For each sale within `registros`, I will try to process it.

        try:
            amount = float(sale["monto"]) # Try to convert the value of `"monto"` to `float`.

        except (ValueError, TypeError):
            print(f"Warning: the sale with ID {sale['id']} was omitted")
            continue

        total_amount += amount
        successful_records += 1

    return total_amount, successful_records


total, successful_records = process_sales(registros_ventas)

print(f"Total amount: ${total}")
print(f"Successfully processed records: {successful_records}")
