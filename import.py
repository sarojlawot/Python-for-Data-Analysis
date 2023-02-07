#comparison opertaor




#the else clause
price1 = 4
if price1 == 0:
    print('free')
else:
    print('not free')

apps_data = [['call of duty : zombies',5.0],['facebook',0.0],['instagram',0.0],['temple run',0.0]]

for app in apps_data:
    price = app[1]
    
    if price == 0.0:
        app.append('free')
        
    if price != 0.0:
        app.append('not free')
        
print(apps_data)
print(len(apps_data))

#using if statement with an else clause
apps_data1 = [['call of duty : zombies',5.0],['facebook',0.0],['instagram',0.0],['temple run',0.0]]

for app in apps_data1:
    price = app[1]
    
    if price == 0.0:
        app.append('free')
    else:
        app.append('not free')
        
print(apps_data1)

#the elif clause
apps_data2 = [['facebook',0.0],['notion',14.99],['astropad standard',29.99],
              ['navigon europe',74.99]]

for app in apps_data2:
    price = app[1]
    
    if price == 0.0:
     app.append('free')
    

    elif price >0.0 and price < 20:
        app.append('affordable')
        
    elif price >= 20 and price < 50:
        app.append('expensive')
        
    elif price >= 50:
        app.append('very expensive') 
        
print(apps_data2) 

#else vs elif
'''
For elif price >= 50, app.append('very expensive') 
will execute only if the price is greater than or equal
to 50. For else, there's no condition to meet
(other than the previous if and elif clauses resolving to False),
and app.append('very expensive') executes even if the price has a 
value of -5 or -100.
'''
apps_data3 = [['facebook',0.0],['notion',14.99],['astropad standard',29.99],
              ['navigon europe',74.99]]
for row in apps_data3:
    price = row[1]
    
    if price == 0.0:
        row.append('free')
    elif price > 0.0 and price < 20:
        row.append('affordable')
    elif price >=20 and price <50:
        row.append('expensive')
    else:
        row.append ('very expensive')
        
print(apps_data3)