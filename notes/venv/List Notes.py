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

#MAKING OUR OWN LIST
Brand = ['Toyota', 'Honda,', 'Ford', 'Chevorlette',]

print("The last thing in the list is %s" % Brand[len(Brand) - 1])

#Mr. Wibe List
ToyotaCarModels = ['corolla', 'camry', 't100', 'tundra', 'cessida',
                   'chicken', 'corollahatch', 'ae86', 'gt86',
                   'crown','hilux', 'tacoma', 'supra', 'celicagts',
                   'sprintertrueno', 'seqouia', '4runner', 'solara',
                   'venza', 'rav4', 'yaris',]

# Slicing
print(ToyotaCarModels[2:5])
print(ToyotaCarModels[3:4])
print(ToyotaCarModels[10:])
print(ToyotaCarModels[:5])

# Adding stuff to a list (part 1)
ToyotaCarModels.append("rav4")
ToyotaCarModels.append("yaris")
print(ToyotaCarModels)
# Everything is in the form Object.method(parameters)

# Adding to a list (Not at the end)
ToyotaCarModels.insert(2, "C-HR")
print(ToyotaCarModels)


#Removing from a list
ToyotaCarModels.remove("t100")
ToyotaCarModels.remove("tundra")
print(ToyotaCarModels)
# This removes the specific item from the list

#Removing from a list (pt 2)
#Sometimes you don't know what is in the list, but you know
#you want to get rid of something at a specific index
ToyotaCarModels.pop(0)
print(ToyotaCarModels)
#Notice that "corolla" is no longer in the list because was it at index 0

#Practice time...


HondaCarmodels = ['civic', 'accord', 'prelude','insight',]
HondaCarmodels.append('civicSI')
print(HondaCarmodels)

HondaCarmodels.remove("accord")
print(HondaCarmodels)


#Finding things in a list
print(ToyotaCarModels.index("chicken"))
# THis printed 9 for me, so chicken must be at index 9.
# This is an easy way of finding things in a list.

# MAKE SURE TO AVOID PUTTING PARENTHESES WHEN MAKING A LIST AND TO
# PUT BRACKETS BECAUSE THEY CANNOT BE CHANGED

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Changing back into a string (list→string)
print("!".join(list))
