import csv


low_stock = []

with open("inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = row["item_name"]
        quantity = int(row["quantity"])
        threshold = int(row["threshold"])
        
        if quantity < threshold :
            low_stock.append(row)

print("====== RESTOCK NEEDED ======")

for item in low_stock:
    print(f"{item['item_name']} - Quantity: {item['quantity']} - Threshold: {item['threshold']}")

with open("restock_report.csv", "w", newline="") as file:
    fieldnames = ["item_name", "quantity", "threshold"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(low_stock)

print("\nRestock saved as restock_report.csv")
