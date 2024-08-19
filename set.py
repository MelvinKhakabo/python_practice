#create empty set
emptySet = set()
print (emptySet)

#create empty directory
emptyDictionary = {}
print(emptyDictionary)

#enter a set
numbers = {2, 4, 6, 8, 8, 2, 4, 6}
print("Initial set:", numbers)
#using add method
numbers.add(10)
print("Updated Set:", numbers)

#update a set
companies = {'Google', 'Amazon', 'Microsoft'}
food_companies = {'Starbucks', 'McDonalds', 'Chipotle', 'McDonalds'}
companies.update(food_companies)
print(companies)

lakes = {'Baringo', 'Nakuru', 'Naivasha', 'Victoria'}
rivers = {'Yala', 'Tana', 'Athi', 'Nile','Tana'}
lakes.update(rivers)
print(lakes)
#remove items from a set
lakes.discard('Nile')
print(lakes)

#for function
for lake in lakes:
    print(lake)

#length of a set
print(len(lakes))