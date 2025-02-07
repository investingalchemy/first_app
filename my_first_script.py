#print("Hello World!")

#Day 3: List and Tuples practice

#Indexing
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21] 
Num_3 = my_list[3]
print(f"It is {Num_3}")

#Slicing
my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
Num_2 = my_list[1:3]
print(Num_2)

#Adding
my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
my_list.append(34)
print(my_list)

#Removing
my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
my_list.remove(1)
print(my_list)

#sorting
my_list = [8, 13, 21, 5, 3, 2, 1 ,1, 0]
my_list.sort()
print(my_list)

#extending
list_a = ['apple', 'pepper']
list_b = ['pineapple', 'watermelon']
list_a.extend(list_b)
print(list_a)

#insert
my_list = [0, 1, 1, 2, 3, 5, 8 ,13, 21]
my_list.insert(3, 37)
print(my_list)

#TOUPLES
#Indexing
my_tuple = (10, 20, 'orange')
print(my_tuple[0])

#slicing
my_tuple = (10, 20, 'orange')
print(my_tuple[0:2])


#length
my_tuple = (10, 20, 'orange')
print(len(my_tuple))

#concatenation (did not work for me)
my_tuple = (10, 20, 'orange')
my_tuple = my_tuple + (30, 40)
print(my_tuple)


#LIST PRACTICE EXCERCISES
#list of favorite movies, using append and remove to adjust list
movies = ["Gladiator", "Eternal Sunshine", "Green Street", "Inception", "Interstellar"]
movies.append("Iron Man")
movies.remove("Green Street")
print(movies)

#indexing and slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[3:5])

#Inserting Items
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
colors.append("purple")
print(colors)

#Truple Pracitce Excercises
#indexing
dimensions = (10, 5, 15)
print(dimensions[1])

 #slicing a truple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[2:6])

#concatenating truples:
fruits = ("apple", "banana")
vegetables = ('carrot', 'lettuce')
groceries = fruits + vegetables
print(groceries)
