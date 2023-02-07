#print(1.00-5)

print("i don't wamma be dumb");

print(0.0+1.99);

print(19-4);

print(4**2);

print(5**8);

result = 1*5/5;
print(result);

result =0
print(result)

result =8
print(result)
if 5>4:
  print("five is greater than two!")
#print("five is greater than two!")#indentation error 


motto ='facebook\'s old motto was "move fast and break things".'#escape character
print(motto)

#single concatenation
print('a'+''+'b')
print('i' + ' ' + 'am' + ' ' + 'saroj')
print('a' *4)


#string conversion
print(float('4.4')+1)
a =1
b=2
print(str(a)+str(b))


''' storing  row  elements into variables '''

row_1 = ["saroj",12,'NRP',0.0] #LIST LENGTH
row_1_length = len(row_1)
print(row_1_length)


# list indexing
track_number_index = 0
print(row_1)
#retrieving values from lists
print(row_1[3])

row_2 = ["facebook",0.0,'USD',2974676,3.5]
row_3 = ["instragram",0.0,'USD',2161558,4.5]
difference =row_3[3]-row_2[3]
average = difference/2
print(difference)
print(average)
#negative indexing
print(row_1[-4])

'''
Negative indexing: the last element has the index number -1,
the second to last element has the index number -2, and so on.
'''

'''retrieving multiple list elements
Each list should contain the name of the app (track_name),
the rating count (rating_count_tot), and the user rating (user_rating).
Don't forget that indexing starts at 0
'''
row_1 = ["facebook",0.0,'USD',2974676,3.5]
row_2 = ["instragram",0.0,'USD',2161558,4.5]
row_3 = ["clash of clans",0.0,'USD',2130805,4.5]
row_4 = ["fruit ninja classic",1.99,'USD',698516,4.5]
row_5 = ["minecraft:pocket edition",6.99,'USD',522012,4.5]
'''
fb_rating_data = [row_1 [0],row_1[-2],row_1[-1]]
inStra_ratinf_data = [row_2[0],row_2[-2],row_2[-1]]
minecraft_rating_data = [row_5[0],row_5[-2],row_5[-1]]
total_rating = fb_rating_data[2]+inStra_ratinf_data[2]+minecraft_rating_data[2]
average_rating = total_rating/3
print(average_rating)

'''
data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set[0])
print(data_set[-1])
print(data_set[:2])



b=6
b/=2
print(int(b))
''' slicing '''
cc_row = row_1[0:4]#slicing 
print(cc_row)
