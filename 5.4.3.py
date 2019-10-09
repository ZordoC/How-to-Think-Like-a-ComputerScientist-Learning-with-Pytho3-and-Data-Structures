

def add_fruit(inventory,fruit,quantity=0):
    '''''
    Adds a key value pair into a dictionary
    
    :input(invetory): dict
    :input(fruit): string
    :input(quantity): int

    :output(iventory):dict
    '''''

    
    inventory[fruit] = quantity

    return inventory


new_inventory = {}




add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)


print(new_inventory)