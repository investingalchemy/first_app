#Default Grocery List
grocery_list = [
    {"name":"milk", "store":"Sprouts", "cost":6.47, "amount": 2, "priority": 1, "buy": True},
    {"name":"eggs", "store":"Costco", "cost":20.99, "amount": 1, "priority": 1, "buy": True},
    {"name":"bread", "store":"Safeway", "cost":2.47, "amount": 2, "priority": 3, "buy": True},
    {"name":"meat", "store":"Costco", "cost":25.95, "amount": 2, "priority": 1, "buy": True},
    {"name":"cheese", "store":"Trader Joe's", "cost":5.99, "amount": 3, "priority": 1, "buy": True}
]
#Add item function to add items to the list
def add_item(name, store, cost, amount, priority, buy):
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}
    grocery_list.append(item)

#Remove item function to remove items from the list
def remove_item(name):
    #finds the index of the name
    index = get_index_from_name(name)
    if index is None:
        print(f"Error: Item '{name}' not found in grocery list.")
        return
    #removes the item from the list
    grocery_list.pop(index)

#function that finds the index of the list from the name
def get_index_from_name(name):
    index = 0

    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1
#function that prints all the items in the grocery list
def list_items():
    for item in grocery_list:
        print(item)     

#function that lets you edit the items in the grocery list
def edit_item(name, store=None, cost=None, amount=None, priority=None, buy="skip"):
    index = get_index_from_name(name)

    old_item = grocery_list[index]

    if not store:
        store = old_item["store"]

    if not cost:
        cost = old_item["cost"]

    if not amount:
        amount = old_item["amount"]

    if not priority:
        priority = old_item["priority"]

    if buy == "skip":
        buy = old_item["buy"]

    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}

    grocery_list[index] = item

#export function that provides the entire list of items and total cost
def export_items():
    buy_list = []

    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)
    
    if buy_list:
        for item in buy_list:
            print(f"name: {item['name']} - store: {item['store']} - cost: ${item['cost']} - amount: {item['amount']} - priority: {item['priority']}")

        total_cost = calculate_total_cost(buy_list, round_cost = True)

        print(f"The total cost is ${total_cost}")

#function to calculate the total cost including tax
def calculate_total_cost(grocery_list, round_cost=False, tax=0.12):
    total_cost = 0

    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    if round_cost:
        total_cost = round(total_cost)

    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    return total_cost

