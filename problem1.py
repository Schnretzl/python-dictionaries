# 1. Real-World Python Dictionary Applications

# Task 1: Restaurant Menu Update
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.99, "Coffee": 1.99}
restaurant_menu["Main Course"]["Steak"] = 17.99
restaurant_menu["Starters"].pop("Bruschetta")

for section in restaurant_menu:
    print(section)
    for item, price in restaurant_menu[section].items():
        print(f"{item}: ${price}")
    #end for
    print('----------------')
#end for