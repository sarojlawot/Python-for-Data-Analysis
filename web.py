'''x = 23
y =23
print(x+y)
'''
''' python for loops
'''

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
'''
app_data_set = [row_1, row_2, row_3, row_4, row_5]
for row in app_data_set:
    rating = row[-2]
    print(rating)
    '''
app_data = [row_1,row_2,row_3,row_4,row_5]
rating_sum = 0
for value in app_data:
    count =value[3]
    rating_sum = rating_sum + count
    print(rating_sum)
'''
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] +
              app_data_set[2][-1] + app_data_set[3][-1] +
              app_data_set[4][-1]) / 5

print(avg_rating)
'''

#for loops
'''
app_rating = [3.5,4.5,4.5,4.5,4.5]
for element in app_rating: #for(like in for element in app_rating:)
    print(element)
    
    
client_name = ['saroj','gops','gopcheng']
for element in client_name:
    print(element)
 '''   
a_list = [1,2,3,4]

a_sum = 0
for value in a_list:
    a_sum = a_sum + value
    print(a_sum)
print(a_sum) 