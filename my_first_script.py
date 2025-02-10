#print("Hello World!")

##Asking for Favorite grocery store
#Favorite_Grocery_Store = input("What is your favorite grocery store?")
#
##Greeting them to store
#print(f"Welcome to {Favorite_Grocery_Store}")

##price of grocery items
#milk = 12.50
#bread = 3.69
#eggs = 5.99
#
##calculating total cost
#total_cost = milk + bread + eggs
#
##Print total cost
#print("The total is: $" + str(total_cost))


#Day 3: List and Tuples practice

#Indexing
#my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21] 
#Num_3 = my_list[3]
#print(f"It is {Num_3}")

#Slicing
#my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
#Num_2 = my_list[1:3]
#print(Num_2)

#Adding
#my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
#my_list.append(34)
#print(my_list)

#Removing
#my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
#my_list.remove(1)
#print(my_list)

#sorting
#my_list = [8, 13, 21, 5, 3, 2, 1 ,1, 0]
#my_list.sort()
#print(my_list)

#extending
#list_a = ['apple', 'pepper']
#list_b = ['pineapple', 'watermelon']
#list_a.extend(list_b)
#print(list_a)

#insert
#my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
#my_list.insert(3, 37)
#print(my_list)

#TOUPLES
#Indexing
#my_tuple = (10, 20, 'orange')
#print(my_tuple[0])

#slicing
#my_tuple = (10, 20, 'orange')
#print(my_tuple[0:2])


#length
#my_tuple = (10, 20, 'orange')
#print(len(my_tuple))

#concatenation (did not work for me)
#my_tuple = (10, 20, 'orange')
#my_tuple = my_tuple + (30, 40)
#print(my_tuple)


#LIST PRACTICE EXCERCISES
#list of favorite movies, using append and remove to adjust list
#movies = ["Gladiator", "Eternal Sunshine", "Green Street", "Inception", "Interstellar"]
#movies.append("Iron Man")
#movies.remove("Green Street")
#print(movies)

#indexing and slicing
#numbers = [10, 20, 30, 40, 50]
#print(numbers[3:5])

#Inserting Items
#colors = ["red", "blue", "green"]
#colors.insert(1, "yellow")
#colors.append("purple")
#print(colors)

#Truple Pracitce Excercises
#indexing
#dimensions = (10, 5, 15)
#print(dimensions[1])

 #slicing a truple
#numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
#print(numbers[2:6])

#concatenating truples:
#fruits = ("apple", "banana")
#vegetables = ('carrot', 'lettuce')
#groceries = fruits + vegetables
#print(groceries)

##practicing dictionaries
#dict_a = {"name":"milk", "cost": 6.5, "store": "Save-On", "amount": 2}
#print(dict_a.items())
#
##practice excercise
##create and accessing values
#book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
#print(book["author"])
#
##Adding and updating entries:
#profile = {}
#profile['name'] = 'Alice'
#profile['age'] = 30
#profile['city'] = 'Paris'
#print(profile)
#profile['city'] = 'London'
#print(profile)
#
##removing and retrieving keys and values
#student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
#student.pop('subject')
#print(student)

## The program has an error, find it and fix it
##milk value was a string not a float, need to convert to float to add with bread, then convert total to string to add to total cost statement.
#milk = "3"
#bread = 2.5
#total = float(milk) + bread
#print("The total cost is: $" + str(total))

##PRACTICING SETS
#
##adding and removing elements in sets
#fruits = {'apple', 'banana', 'cherry'}
#fruits.add('orange')
#fruits.remove('banana')
#print(fruits)
#
##Union and Intersections
#set_a = {1, 2, 3, 4}
#set_b = {3, 4, 5, 6}
#print(set_a.union(set_b))
#
#print(set_a.intersection(set_b))
#
#
##Difference Operation
#set_x = {'cat', 'dog', 'fish'}
#set_y = {'dog', "bird"}
#print(set_x.difference(set_y))

##DAY 3
##Threee Tuples to represent grocery items
#apple_tuple = ('apple', 0.50, 5)
#orange_tuple = ('orange', 0.75, 8)
#pineapple_tuple = ('pineapple', 1.30, 10)
#
##Grocery list
#grocery_list = []
#grocery_list.append(apple_tuple)
#grocery_list.append(orange_tuple)
#grocery_list.append(pineapple_tuple)
#print(grocery_list[0])
#
##Total cost of apples
#total_cost = apple_tuple[1] * apple_tuple[2]
#print(f"Total cost of apples: ${total_cost}")
#
##total cost of oranges
#total_cost = orange_tuple[1] * orange_tuple[2]
#print(f"Total cost of oranges: ${total_cost}")
#
##total cost of pineapples
#total_cost = pineapple_tuple[1] * pineapple_tuple[2]
#print(f"Total cost of Pineapples: ${total_cost}")
#
#
##Dictionaries
#apple_dict = {'name':'Apple', 'price': 0.50, 'quantity': 5}
#orange_dict = {'name':'Orange', 'price': 0.75, 'quantity': 8}
#pineapple_dict = {'name':'Pineapple', 'price': 1.37, 'quantity': 13}
#
##adding total cost to dictionaries
#apple_dict['Total Cost'] = round(apple_dict['price'] * apple_dict['quantity'], 2)
#print(apple_dict)
#
#orange_dict['Total Cost'] = orange_dict['price'] * orange_dict['quantity']
#print(orange_dict)
#
#pineapple_dict['Total Cost'] = round(pineapple_dict['price'] * pineapple_dict['quantity'], 2)
#print(pineapple_dict)
#
#print(f"Total cost of apples: ${apple_dict['Total Cost']}")
#print(f"Total cost of oranges: ${orange_dict['Total Cost']}")
#print(f"Total cost of pineapples: ${pineapple_dict['Total Cost']}")
#
#
##EXCERCISE 3 Slicing and Sorting a List
#num_list = [16, 47, 1, 3, 5, 9, 15, 2]
##slice and print everything from the second index onward
#print(num_list[2:])
##slice and print everything up to, but not including, the fourth index
#print(num_list[:4])
##use a negative index to get and print the third to last item in the list
#print(num_list[-3])
#
##sort and print the number list in descending order
#num_list.sort(reverse=True)
#print(num_list)
##prints lengh of number list
#print(len(num_list))
#
##EXCERCISE 4 SETS OPERATIONS
#dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
#desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}
#dairy_products.add('ice cream')
#desserts.add('ice cream')
#dairy_products.remove('yogurt')
#desserts.remove('jello')
#
#print(dairy_products)
#print(desserts)
#print(dairy_products.intersection(desserts))

#DAY 4 LESSON EXERCISES
#Conditional Statements
#Even/Odd Number identifier
#number = int(input("Give me a number:"))

#if number % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

#Temperature categorizer
#temperature = int(input('what temperature is it?'))

#if temperature <= 60:
#    print("That's Cold!")
#elif temperature > 60 and temperature <75:
#    print("That's warm")
#else:
#    print("That's HOT!")

#Voter Eligebility
#age = int(input("Enter your age: "))
#citizenship = input("Are you a citizen? (yes/no): ").lower()

#if age >= 18:
#    if citizenship == "yes":
#        print("Eligible to vote")
#    else:
#        print("Not Eligible: Must be a citizen")
#else:
#    print("Not eligible: Must be 18 or older")

#FOR AND WHILE LOOPS
#grocery list
#groceries_list = ["eggs", "bread", "sugar"]
#print items in grocery list
#for grocery in groceries_list:
#   print(grocery)

#while loop with user input
#grocery list
#grocery_list = ["eggs", "bread", "sugar"]
#while loop to add items
#while True:
#    command = input("Type a command, add or done: ")
#    if command == "done":
 #       break
#
#    add_item = input("Add a grocery item: ")
#    grocery_list.append(add_item)
#    print(f"{add_item} was added to the grocery list!")
#    print(grocery_list)
#print(f"The full grocery list is: {grocery_list}")

#Loop through a Dictionary and print each items name and total cost
#grocery_list = [
#    {"name":"eggs", "amount": 5, "cost": 2.5, "store": "Safeway"},
#    {"name":"bread", "amount": 3, "cost": 3.5, "store": "Trader Joe's"},
#    {"name":"sugar", "amount": 1, "cost": 1.5, "store": "Costco"}
#]
#
#for item in grocery_list:
#    total_cost = item["amount"] * item["cost"]
#    print(f"The total cost of the {item["name"]} is: ${total_cost}")

#LOOP CONTROL
#Using Break to stop a loop when a specific item is found in a list
#for item in ["apples", "bananas", "carrots", "eggs", "meat"]:
#    if item == "meat":
#       break
#print(f"{item} is carnivore diet")

#Using continue to skip specific items in a grocery list
#carnivore_diet = ["meat", "eggs", "milk", "cheese"]
#banned_foods = []

#for item in ["apples", "bananas", "carrots", "eggs", "meat"]:
#    if item in carnivore_diet:
#        continue
#    banned_foods.append(item)
#if len(banned_foods) >= 2:
#    print (f"{banned_foods} are not allowed in the carnivore diet!")
#elif len(banned_foods) == 1:
#    print(f"{banned_foods} is not allowed in the carnivore diet!")
#else:
#    print("This grocery list is pure carnivore diet!")
#

#Using pass for an item to act as a placeholder for future code
#for item in ["apples", "bananas", "carrots", "eggs", "meat"]:
#    if item == "meat":
#        pass
#    print(item)

#Using Try-Except to handle errors gracefully
#number = input("Enter a number: ")

#try:    
#    entered_number = int(number)
#    print(f"{entered_number} is the number you entered")
#except (ValueError) as e:
#    print(f"ERROR: Please enter a valid number")

#practicing traceback identification
#a = 10
#b = 5
#double_b = b * 2
#total = a + double_b
#print("The total is:", total)


#DAY 4 REQUIRED ASSIGNMENTS

#EXERCISE 1 CATEGORIZATION
#Catagorizing grocery items between food items, non food items, and unknown inputs

#food_items = ["apple", "bread", "milk"]
#non_food_items = ["soap", "detergent", "towels"]
#grocery_items = []

#inputted_item = input("Add a grocery item to the list: ")
#grocery_items.append(inputted_item)

#if inputted_item in food_items:
##    print(f"{inputted_item} is a food item")
##elif inputted_item in non_food_items:
##    print(f"{inputted_item} is not a food item!")
##else:
##    print(f"{inputted_item} in an unknown item")

#EXERCISE 2 Making a burger with a while loop

#checking to see if you can make burger and fries with your budget
#items_list = [
#    {"name": "fries", "cost":6.25, "amount": 1},
#    {"name": "burger patties", "cost":13.50, "amount": 1},
#    {"name": "burger buns", "cost":3.50, "amount": 2},
#    {"name": "tomato", "cost":1.50, "amount": 2},
#    {"name": "lettuce", "cost":5, "amount": 1},
#    {"name": "Ketchup", "cost":3.47, "amount": 1},
#    {"name": "pickles", "cost":4.25, "amount": 1}
#]
#shopping_list = []
#budget = 27.5
#total_cost = 0
#index = 0
#
#while total_cost <= budget:
#    item = items_list[index]
#    item_name = item["name"]
#    item_subtotal = (item["cost"]) * item["amount"]
#
#    if total_cost + item_subtotal > budget:
#        break
#
#    shopping_list.append(item_name)
#    total_cost += item_subtotal
#    index += 1
#
#print("Shopping List: ", shopping_list)

#EXERCISE 3: Extending Logic with Nesting
#printing items as they are being added to the grocery list
#items_list = [
#    {"name": "fries", "cost":6.25, "amount": 1},
#    {"name": "burger patties", "cost":13.50, "amount": 1},
#    {"name": "burger buns", "cost":3.50, "amount": 2},
#    {"name": "tomato", "cost":1.50, "amount": 2},
#    {"name": "lettuce", "cost":5, "amount": 1},
#    {"name": "Ketchup", "cost":3.47, "amount": 1},
#    {"name": "pickles", "cost":4.25, "amount": 1}
#]
#shopping_list = []
#budget = 27.5
#total_cost = 0
#index = 0
#
#while total_cost <= budget:
#    item = items_list[index]
#    item_name = item["name"]
#    item_subtotal = (item["cost"]) * item["amount"]
#
#    if total_cost + item_subtotal > budget:
#        break
#
#    shopping_list.append(item_name)
#    total_cost += item_subtotal
#    index += 1
#
#    for item in shopping_list:
#        print(item)
#    print("----------")
#
#print("Shopping List: ", shopping_list)

#EXERCISE 4: Breaking the Loop
#See if we have enough to make at least burger and fries
#items_list = [
#    {"name": "fries", "cost":6.25, "amount": 1},
#    {"name": "burger patties", "cost":13.50, "amount": 1},
#    {"name": "burger buns", "cost":3.50, "amount": 2},
#    {"name": "tomato", "cost":1.50, "amount": 2},
#    {"name": "lettuce", "cost":5, "amount": 1},
#    {"name": "Ketchup", "cost":3.47, "amount": 1},
#    {"name": "pickles", "cost":4.25, "amount": 1}
#]
#shopping_list = []
#budget = 27.5
#total_cost = 0
#index = 0
#
#while total_cost <= budget:
#    item = items_list[index]
#    item_name = item["name"]
#    item_subtotal = (item["cost"]) * item["amount"]
#
#    if total_cost + item_subtotal > budget:
#        break
#
#    shopping_list.append(item_name)
#    total_cost += item_subtotal
#    index += 1
#
#    for item in shopping_list:
#        print(item)
#    print("----------")
#
#    if "burger buns" in shopping_list and "burger patties" in shopping_list and "fries" in shopping_list:
#        print(f"We can make burgers and fries for {total_cost}")
#        break
#
#print(shopping_list)

#EXERCISE 5: Error Handling with Try-Except
#items_list = [
#    {"name": "fries", "cost":6.25, "amount": 1},
#    {"name": "burger patties", "cost":13.50, "amount": 1},
#    {"name": "burger buns", "cost":3.50, "amount": 2},
#    {"name": "tomato", "cost":1.50, "amount": 2},
#    {"name": "lettuce", "cost":5, "amount": 1},
#    {"name": "Ketchup", "cost":3.47, "amount": 1},
#    {"name": "pickles", "cost":4.25, "amount": 1}
#]
#shopping_list = []
#budget = 27.5
#total_cost = 0
#index = "0"
#
#while total_cost <= budget:
#    try:
#        item = items_list[index]
#        item_name = item["name"]
#        item_subtotal = (item["cost"]) * item["amount"]
#
#        if total_cost + item_subtotal > budget:
#            break
#
#        shopping_list.append(item_name)
#        total_cost += item_subtotal
#        index += 1
#
#        for item in shopping_list:
#            print(item)
#        print("----------")
#
#        if "burger buns" in shopping_list and "burger patties" in shopping_list and "fries" in shopping_list:
#            print(f"We can make burgers and fries for {total_cost}")
#            break
#
#    except (ValueError, TypeError):
#        print("ERROR: The index must be an integer")
#        break
#
#print(shopping_list)

#EXERCISE 6: Customize your script
#used my own recipe to see if I had enough budget to make a steak
#items_list = [
#    {"name": "steak", "cost":16.25, "amount": 1},
#    {"name": "rosemary", "cost":1.50, "amount": 1},
#    {"name": "salt", "cost":0.50, "amount": 1},
#    {"name": "gravy", "cost":1.50, "amount": 1},
#    {"name": "potatoes", "cost":2, "amount": 1},
#    {"name": "bbq sauce", "cost":31., "amount": 1}
#]
#shopping_list = []
#budget = 18.50
#total_cost = 0
#index = 0
#
#while total_cost <= budget:
#    try:
#        item = items_list[index]
#        item_name = item["name"]
#        item_subtotal = (item["cost"]) * item["amount"]
#
#        if total_cost + item_subtotal > budget:
#            break
#
#        shopping_list.append(item_name)
#        total_cost += item_subtotal
#        index += 1
#
#        for item in shopping_list:
#            print(item)
#        print("----------")
#
#        if "steak" in shopping_list and "rosemary" in shopping_list and "salt" in shopping_list:
#            print(f"We can make a steak for {total_cost}")
#            break
#
#    except (ValueError, TypeError):
#        print("ERROR: The index must be an integer")
#        break
#
#print(shopping_list)

#DAY 5 EXERCISES AND REQUIRED ASSIGNMENTS
#Defining & calling functions
#Exercise 1:Displaying a message
#def welcome_message():
#    print("Welcome!")
#welcome_message()
#
##Exercise 2: Print favorite food
#def favorite_food():
#    print("Steak and cheese are my favorite foods")
#favorite_food()
##Exercise 3: Show sum of numbers
#def show_sum():
#    results = 5 + 10
#    print (results)
#show_sum()

#Paramaters and return values
#Exercise 1: Grocery Item Search, prints whether an item is available
#
#def find_item(item_name, is_available):
#    if is_available == True:
#        print(f"{item_name} is available")
#    else:
#        print(f"{item_name} is not available")
#
#find_item("Water", True)
##Exercise 2: Favorite Snack, shows how much snacks are left
#def favorite_snack(snack_name, quantity_left):
#    if quantity_left > 0:
#        print(f"You have some {snack_name} left to enjoy")
#    else:
#        print(f"You're out of {snack_name}")
#
#favorite_snack("Chips", 3)
#favorite_snack("Cookies", 0)
#
##Exercise 3: Store Item Location; where to find items in a store
#
#def item_location (item_name, store_selection):
#    print (f"Find {item_name} in the {store_selection}")
#
#item_location("Juice", "Beverage Aisle")
#
#Scope and Lifetime of Variables
#Exercise 1: Local and Global Variables, showing difference between local and global variable placement
#food = "Ribs"
#
#def favorite_food():
#    food = "Steak"
#    print("Local food: ", food)
#
#favorite_food()
#print("Global food:", food)
#
##Exercise 2: Variable Lifetime in functions by observing results
#
#def counter():
#    count = 0
#    count += 1
#    print("Count: ", count)
#
#counter()
#counter()
#
#Exercise 3: Combining scope and lifetime to see the effects on variable values
#user_name = "Joe"
#
#def change_name():
#    user_name = "James"
#    print("Inside function:", user_name)
#
#change_name()
#print("Outside function:", user_name)

from datetime import date
print(date.today())

