#if ,else,elif statements
'''  if statements  '''
a = 56
b = 44
if a > b:
    print(" a is greater than b ")
 
c = 44
d = 44
if d > c:
    print("d is greater than c")
elif c == d:
    print(" c and d are equal ")
    
#  if statements in data 

row_1 = ["facebook",0.0,'USD',2974676,3.5]
row_2 = ["instragram",0.0,'USD',2161558,4.5]
row_3 = ["clash of clans",0.0,'USD',2130805,4.5]
row_4 = ["fruit ninja classic",1.99,'USD',698516,4.5]
row_5 = ["minecraft:pocket edition",6.99,'USD',522012,4.5]

apps_data = [row_1,row_2,row_3,row_4,row_5]
rating =[]
for row in apps_data:
    price = float(row[4])
    rating.append(price)
print(rating[:5])


price_1 = 2
print(price_1 != 0)
print(price_1 != 2)

if price_1 != 0:
    print('not free')
if price_1 != 2:
    print('price is not equal')
