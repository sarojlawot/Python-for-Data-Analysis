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
'''  From Python's perspective, dictionaries are defined as objects with the data type 'dict':
     <class 'dict'>
'''
print(type(thisdict))