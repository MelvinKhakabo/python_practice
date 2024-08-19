#list content
list_a = [1, 2, 3, 4, 5]

#lists must be indexed
#index   0 1 2 3 4 5 6 7 8 9 

# to print a specific item on the list
print(list_a[2])
print(list_a[0])

#modifying lists
print(list_a)
list_a[0] = 10
print(list_a)

#getting the length
print(len(list_a)) 
#insert into the list
list_a.insert(len(list_a), 6)
print(list_a)

#append(adding things to a list)
list_a.append(7)
print(list_a)

#extend(adding a list of items to the list)
list_a.extend([8,9,10])
print(list_a)

#pop(delete item from list)
list_a.pop(3)
print(list_a)

#finding all items in your list
for item in list_a :
    print(item)
