#print("Hello World!")

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
