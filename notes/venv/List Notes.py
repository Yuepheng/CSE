# Creating a list
fruit = ['apples', 'oranges', 'blackberries', 'strawberries',
         'blueberries','pineapple','watermellon','coconut', 'Jackfruit',]  # USE SQUARE BRACKETS!!!!!!!!
print(fruit)

# Pulling items from a list
print(fruit[1])

# Getting the lenth of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'watermellon'
print(fruit)

# Looping through Lists
for item in fruit:
    print(item)

#MAKING OUT OWN LIST
Brand = ['Toyota', 'Honda,', 'Ford', 'Chevorlette',]

print("The last thing in the list is %s" % Brand[len(Brand) - 1])
