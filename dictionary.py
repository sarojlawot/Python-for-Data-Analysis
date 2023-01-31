'''
#in this lesson we will learn how to create dictionaries
content_rating = ['4+','7+','12+','17+']
numbers = [4433,987,1155,622]

content_rating_numbers = [['4+','7+','12+','17+'],[4433,987,1155,622]]
print(content_rating_numbers)

#create and print dictionary
thisdict = {
    "brand":"food",
    "model":"mustang",
    "year":1964 ,
    "year":2023   
}
print(thisdict)
#To determine how many items a dictionary has, use the len() function:
print(len(thisdict))
##### type()
##### From Python's perspective, dictionaries are defined as objects with the data type 'dict':
###  <class 'dict'>

print(type(thisdict))

### the dict() constructor
thisdict =dict(name = "john",age = 36,country = "nepal")
print(thisdict)

# Accessing items
dictor= {
     "brand":"gucchi",
     "model":"yfc2",
     "price":'$120',
     "year":2023
 }
x = dictor["price"]
print(x)

### there is also a method called get() that will give you the same result:
x = dictor.get('model')
print(x)

# keys()method will return a list of all the keys in the dictionary
x = dictor.keys()
print(x)

### Add a new items

car = {
    "brand":'BMW',
    "model":"hifi",
    "year":2021
}
x = car.keys()
print(x)
# Before the change

car["color"] = "red"

print(x)

### get values

x = car.values()

car["year"] = 2024
print(x)

### Items
x = car.items()
print(x)

car["year"] = 2020
print(x)


###check if key exists

bus = {
    "brand":"toyota",
    "model":"bhgg",
    "color":"black"
}
w = bus.items()
print(w)

if "model" in bus:
    print("yes,'model' is one of the keys in tha bus dictionary")
    
########################################################################################
# change values

book = {
    "name":"rich daddy",
    "pages":202,
    "editions":"4th"
}
book["pages"] = 300  ##change
print(book)
 ### updates dictionary
 
book.update({"name":"rich babe"})
print(book)

#########################################################
### adding items

mobile = {
    "model":"nord 2",
    "color":"blue",
    "lunch":2019
}
mobile["brand"] = 'one plus'
print(mobile)


mobile.update({"color":"mate black"})
print(mobile)


####  REMOVEING ITEMS  #########

mobile.pop("color")
print(mobile)


mobile.popitem()
print(mobile)

mobile.popitem() ##### one by one pop out
print(mobile)


del mobile ["model"] #### delete the dictionary
print(mobile)
### book variable clear ###
book.clear()
print(book)




###########################################################################################
### LOOP  DICTIONARIES ###
laptop = {
    "brand":"acer",
    "model":"aspire 7",
    "year":2019
}

## print key name in dictionary
for x in laptop:
    print(x)
    
## print values
for x in laptop:
    print(laptop[x])
    
    
### loop through both key and values by items()

for x,y in laptop.items():
    print(x,y)
    


##################################################################################3
## COPY  DICTIONARIES
bike = {
    "model":"pulsar 150",
    "year":2112
}
q = bike.copy()
print(q)

#### make a copy of a dictionary with the dict():
q = dict(bike)
print(q)


######################################################################################
##### NESTED DICTIONARIES

my_family = {
    "child1": {
        "name":"fin",
        "age":12
    },
    "child2":{
        "name":"drawft",
        "age":10
    }
}
print (my_family)


'''

##############################################################
#### Alternative  way to create a dictionary ####
content_rating = {}
content_rating['4+']= 1155
content_rating['5+']=987

print(content_rating)


###################################
# checking for membership

content_rating ={'4+':4433,'9+':987,'12+':1155,'17+':622}
print('10+' in content_rating)
#For instance, checking if the string '10+' exists in the 
# dictionary content_ratings returns False because there's 
# no dictionary key '10+' in content_ratings.

is_in_dictionary_1 = '9+' in content_rating
is_in_dictionary_2 = 987 in content_rating
if '17+' in content_rating:
    result = "it exists"
    print(result)
