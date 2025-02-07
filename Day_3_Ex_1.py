#Threee Tuples to represent grocery items
apple_tuple = ('apple', 0.50, 5)
orange_tuple = ('orange', 0.75, 8)
pineapple_tuple = ('pineapple', 1.30, 10)

#Grocery list
grocery_list = []
grocery_list.append(apple_tuple)
grocery_list.append(orange_tuple)
grocery_list.append(pineapple_tuple)
print(grocery_list[0])

#Total cost of apples
total_cost = apple_tuple[1] * apple_tuple[2]
print(f"Total cost of apples: ${total_cost}")

#total cost of oranges
total_cost = orange_tuple[1] * orange_tuple[2]
print(f"Total cost of oranges: ${total_cost}")

#total cost of pineapples
total_cost = pineapple_tuple[1] * pineapple_tuple[2]
print(f"Total cost of Pineapples: ${total_cost}")


#Dictionaries
apple_dict = {'name':'Apple', 'price': 0.50, 'quantity': 5}
orange_dict = {'name':'Orange', 'price': 0.75, 'quantity': 8}
pineapple_dict = {'name':'Pineapple', 'price': 1.37, 'quantity': 13}

#adding total cost to dictionaries
apple_dict['Total Cost'] = round(apple_dict['price'] * apple_dict['quantity'], 2)
print(apple_dict)

orange_dict['Total Cost'] = orange_dict['price'] * orange_dict['quantity']
print(orange_dict)

pineapple_dict['Total Cost'] = round(pineapple_dict['price'] * pineapple_dict['quantity'], 2)
print(pineapple_dict)

print(f"Total cost of apples: ${apple_dict['Total Cost']}")
print(f"Total cost of oranges: ${orange_dict['Total Cost']}")
print(f"Total cost of pineapples: ${pineapple_dict['Total Cost']}")


#EXCERCISE 3 Slicing and Sorting a List
num_list = [16, 47, 1, 3, 5, 9, 15, 2]
#slice and print everything from the second index onward
print(num_list[2:])
#slice and print everything up to, but not including, the fourth index
print(num_list[:4])
#use a negative index to get and print the third to last item in the list
print(num_list[-3])

#sort and print the number list in descending order
num_list.sort(reverse=True)
print(num_list)
#prints lengh of number list
print(len(num_list))

#EXCERCISE 4 SETS OPERATIONS
dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}
dairy_products.add('ice cream')
desserts.add('ice cream')
dairy_products.remove('yogurt')
desserts.remove('jello')

print(dairy_products)
print(desserts)
print(dairy_products.intersection(desserts))

#EXCERCISE 5 UPDATING THE CHANGELOG






