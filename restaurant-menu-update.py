'''
Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

Problem Statement: Given the initial menu:
- Add a new category called "Beverages" with at least two items.

- Update the price of "Steak" to 17.99.

- Remove "Bruschetta" from "Starters". 
'''
import copy

def display_menu(menu_dict): 
    for category, items in menu_dict.items(): 
        print(f"   {category}: ")
        for item, prices in items.items(): 
            print(f"      {item} - {prices}") 
             
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

new_menu = copy.deepcopy(restaurant_menu)  

new_menu["Beverages"] = {"Coke" : 2.99, "Dr. Pepper" : 2.99, "Sprite" : 2.99}   # adding 'Beverages' menu category with dictionary of drinks and prices

new_menu["Main Course"]["Steak"] = 17.99   # updating the price of 'Steak' in 'Main Course' 

del new_menu["Starters"]["Bruschetta"]   # removing 'Bruschetta' from 'Starters' list

print("Old Menu - ")   # display the old menu to see changes implied 

display_menu(restaurant_menu)

print("New Menu - ")   # display new menu with changes 

display_menu(new_menu) 

