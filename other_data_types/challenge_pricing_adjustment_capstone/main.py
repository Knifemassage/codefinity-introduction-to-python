#Define grocery_inventory with the following items and details:
grocery_inventory = {
    "Milk":("Dairy", 3.5, 8),
    "Eggs":("Dairy", 5.50, 30),
    "Bread":("Bakery", 1.50, 50),
    "Apples":("Produce", 1.50, 50)
}
#Check and Update Price/ #Get the price of "Eggs".
price_of_Eggs = grocery_inventory.get("Eggs")[1]
#Get the price of "Eggs".
if price_of_Eggs > 5:
    print(f"Eggs are too expensive, reducing the price by $1.")
    cat, _, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (cat, price_of_Eggs -1, stock)
else: 
    print(f"The price of Eggs is reasonalble")
# 3.Add a New Item
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes:", grocery_inventory)
#Manage Stock
price_of_Milk = (grocery_inventory["Milk"][2])
if price_of_Milk < 10:
    print(f"Milk needs to be restocked. Increasing stock by 20 units.")
    cat, price, _ = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (cat, price, price_of_Milk + 20)
else:
    print("Milk has sufficient stock")
#Remove Item Based on price_of_Eggs
price_of_Apples = grocery_inventory["Apples"][1]
if price_of_Apples > 2:
    print(f"Apples removed from inventory due to high price.")
    grocery_inventory.pop("Apples")

print(f"Updated inventory:", grocery_inventory)

