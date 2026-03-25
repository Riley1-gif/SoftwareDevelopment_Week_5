unique_ID = 1000
inventory = {}

def add_inventory_item():
    global unique_ID
    
    print("\nAdding Inventory Item\n")
    
    item_name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price_per_unit = float(input("Price per item: $"))
    
    item_ID = unique_ID
    unique_ID += 1
    
    inventory[item_ID] = {
        "ID": item_ID,
        "name": item_name,
        "quantity": quantity,
        "price": price_per_unit
    }
    return item_name, item_ID, quantity, price_per_unit


def calculate_total_value():
    # STEP 1: call the first function AND capture the returned values
    item_name, item_ID, quantity, price_per_unit = add_inventory_item()
    
    # STEP 2: calculate total
    total_value = quantity * price_per_unit
    
    # STEP 3: display nicely
    print("\n--- Inventory Summary ---")
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_ID}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ${price_per_unit:.2f}")
    print(f"Total Value: ${total_value:.2f}")
    
    # STEP 4: return the total
    return total_value


def update_inventory():
    item_id = int(input("Enter the Item ID to update: "))

    if item_id in inventory:
        new_quantity = int(input("Enter the new Quantity of the product: "))
        new_price = float(input("Ennter the new Price per item: "))
        print("Item Details updated !")
        inventory[item_id]["quantity"] = new_quantity
        inventory[item_id]["price"] = new_price
        
    else:
        print("Item not found")

def display_inventory_item():
    print("Displaying Inventory Item: \n ")
    item_id = int(input("Enter the Item ID to view the details: "))

    if item_id in inventory:
        item = inventory[item_id]
        id = item["ID"]
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price
        print(f"Item Name: {name}")
        print(f"Item ID: {id}")
        print(f"Quantity: {quantity}")
        print(f"Price per item: {price}")
        print(f"Total Value: ${total}")



# Run it
calculate_total_value()
update_inventory()
display_inventory_item()

