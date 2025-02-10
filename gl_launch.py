import gl_core

def launch():
    #Welcome message
    print("Welcome to The Grocery List App, we are here to help you stay in budget!")
    while True:
        #Starting prompt
        command = input("Enter a command for your grocery list (add, remove, edit, list, export, quit): ")

        if command == "add":
            print("To add an item provide the following details: ")
            name, store, cost, amount, priority, buy = get_inputs()
            gl_core.add_item(name=name, store=store, cost=cost, amount=amount, priority=priority, buy=buy)

        if command == "remove":
            name = input("Enter the name of the item to remove: ")

            gl_core.remove_item(name)

        if command == "edit":
            print("Enter the name of an existing that you would like to edit: ")
            name, store, cost, amount, priority, buy = get_inputs()

            gl_core.edit_item(name, store, cost, amount, priority, buy)

        if command == "list":
            print("These are the current items in your grocery list")
            gl_core.list_items()

        if command == "export":
            print("Here is the final list with total cost: ")
            gl_core.export_items()

        if command == "quit":
            ("Thank you for using The Grocery App, have a great day!")
            break

def get_inputs():
    while True:
        name = input("item name: ")
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:
        store = input("Store name: ")
        if store == "skip":
            store = None
            break
        elif store:
            store = store
            break
        print("Invalid input. Please add a valid store name")

    while True:
        try:
            cost = input("Enter the item price (i.e. 5.50): ")
            if cost == "skip":
                cost = None
                break
            else:
                cost = float(cost)
                break
        except ValueError:
            print("Invalid input. Please enter a valid price")

    while True:
        try:
            amount = input("Item quantity: ")
            if amount == "skip":
                amount = None
                break
            elif int(amount) > 0:
                amount = int(amount)
                break
            else:
                print("Quantity must be a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid quantity")

    while True:
        try:
            priority = input(("Enter a priority rating from 1 to 5: "))
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

    while True:
        try:
            buy = input("Buy: ")
            if buy.lower() == "true":
                buy = True
                break
            elif buy.lower() == "false":
                buy = False
                break
            elif buy == "skip":
                buy = "skip"
                break
            else:
                print("Invalid input. Please enter true or false")
        except ValueError:
            print("Invalid input. Please enter 'true' or 'false' ")
    
    return name, store, cost, amount, priority, buy

if __name__ == "__main__":
    launch()
