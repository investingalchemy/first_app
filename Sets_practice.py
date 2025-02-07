#PRACTICING SETS

#adding and removing elements in sets
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.remove('banana')
print(fruits)

#Union and Intersections
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))

print(set_a.intersection(set_b))


#Difference Operation
set_x = {'cat', 'dog', 'fish'}
set_y = {'dog', "bird"}
print(set_x.difference(set_y))
