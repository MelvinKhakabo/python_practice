# create a languages list
languages = ['Python', 'R','Swift', 'Java']
print(languages)

#print language index 2
languages [2] = 'C'
print(languages)

#delete language from list
del languages [0]
print(languages)

#add a list of othe languages to the list
languages.extend(['Kotlin', 'PHP', 'html'])
print(languages)

#delete a list of languages at specific indexes
del languages [2:3]
languages.remove('html')
print(languages)

#for function
for items in languages:
    print(items)