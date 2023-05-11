# Menu data
menu = {
    '1': {'name': 'Tea'},
    '2': {'name': 'Coffee'},
    '3': {'name': 'Soft Drinks'}
}

tea_menu = {
    '1': {'name': 'Bubble Tea', 'price': 25},
    '2': {'name': 'Green Tea', 'price': 30},
    '3': {'name': 'Thai Tea', 'price': 25},
    '4': {'name': 'Black Tea', 'price': 25}
}

coffee_menu = {
    '1': {'name': 'Americano', 'price': 30},
    '2': {'name': 'Cappuccino', 'price': 35},
    '3': {'name': 'Espresso', 'price': 30},
    '4': {'name': 'Latte', 'price': 35}
}

soft_drink_menu = {
    '1': {'name': 'Coke', 'price': 15},
    '2': {'name': 'Pepsi', 'price': 15},
    '3': {'name': 'Sprite', 'price': 15}
}

# Display main menu
def display_menu():
    print("Welcome to the Vending Machine")
    for key, item in menu.items():
        print(key + " - " + item['name'])

# Display tea menu
def display_tea_menu():
    print("Tea Menu")
    for key, item in tea_menu.items():
        print(key + " - " + item['name'] + " (" + str(item['price']) + " ฿)")

# Display coffee menu
def display_coffee_menu():
    print("Coffee Menu")
    for key, item in coffee_menu.items():
        print(key + " - " + item['name'] + " (" + str(item['price']) + " ฿)")

# Display soft drink menu
def display_soft_drink_menu():
    print("Soft Drink Menu")
    for key, item in soft_drink_menu.items():
        print(key + " - " + item['name'] + " (" + str(item['price']) + " ฿)")

# Process menu selection
def process_menu_selection(selection):
    if selection == '1':
        display_tea_menu()
        tea_selection = input("Enter your tea selection (1, 2, 3, or 4): ")
        process_tea_selection(tea_selection)
    elif selection == '2':
        display_coffee_menu()
        coffee_selection = input("Enter your coffee selection (1, 2, 3, or 4): ")
        process_coffee_selection(coffee_selection)
    elif selection == '3':
        display_soft_drink_menu()
        soft_drink_selection = input("Enter your soft drink selection (1, 2, or 3): ")
        process_soft_drink_selection(soft_drink_selection)
    else:
        print("Invalid selection. Try again.")

# Process tea selection
def process_tea_selection(selection):
    item = tea_menu.get(selection)
    if item:
        print("You have selected:", item['name'])
        amount_due = item['price']
        amount_paid = float(input("Please insert money (" + str(amount_due) + " ฿): "))
        if amount_paid < amount_due:
            print("Invalid amount. Try again.")
        else:
            change = amount_paid - amount_due
            print("Thank you for your purchase!")
            if change > 0:
                print("Your change: (" + str(change) + " ฿)")
    else:
        print("Invalid selection. Try again.")

# Process coffee selection
def process_coffee_selection(selection):
    item = coffee_menu.get(selection)
    if item:
        print("You have selected:", item['name'])
        amount_due = item['price']
        amount_paid = float(input("Please insert money (" + str(amount_due) + " ฿): "))
        if amount_paid < amount_due:
            print("Invalid amount. Try again.")
        else:
            change = amount_paid - amount_due
            print("Thank you for your purchase!")
            if change > 0:
                print("Your change: (" + str(change) + " ฿)")
    else:
        print("Invalid selection. Try again.")

# Process soft drink selection
def process_soft_drink_selection(selection):
    item = soft_drink_menu.get(selection)
    if item:
        print("You have selected:", item['name'])
        amount_due = item['price']
        amount_paid = float(input("Please insert money (" + str(amount_due) + " ฿): "))
        if amount_paid < amount_due:
            print("Invalid amount. Try again.")
        else:
            change = amount_paid - amount_due
            print("Thank you for your purchase!")
            if change > 0:
                print("Your change: (" + str(change) + " ฿)")
    else:
        print("Invalid selection. Try again.")

# Main program
display_menu()
selection = input("Enter your selection (1, 2, or 3): ")
process_menu_selection(selection)





