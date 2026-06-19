# Inventory Management

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print("Inventory Items:")
for item, qty in inventory.items():
    print(item, "-", qty)

# Add new item
inventory["Monitor"] = 8

# Update quantity
inventory["Mouse"] = 30

print("\nUpdated Inventory:")
for item, qty in inventory.items():
    print(item, "-", qty)
