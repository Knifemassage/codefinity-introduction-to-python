# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
# slicing the above strings
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[0:11]
category2 = categories[13:]
bubblegum_price: str = "$1.50"
chacolate_price: str = "$2.00"
pasta_price: str = "$5.40"

print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chacolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")