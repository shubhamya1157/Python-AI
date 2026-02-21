#In buid DataStructur

#1 List

'''
list = [10,"shubham",10.9,True]
'''
'''
print(list)

for i in range(len(list)):
    print(list[i])

list[1] = "shubham yadav"
print(list)
'''

'''
list.append(1157)
print(list)

'''
1
'''
list.insert(0,"Hacker")
print(list)

'''

'''
list.extend([12,23,67]) # Add this element at last
print(list)

'''

'''
list.extend([12,13,12,12])
print(list)

'''

'''
list.remove(12)
print(list)

'''

'''
list.remove(12)
# list.remove(9) -> show error because 9 is't belong to list
print(list)

'''

'''

del_num = list.pop() #remove from last and store
print(list,del_num)

'''

'''
first_ele = list.pop(0) # delete at index 0 and store
print(list,del_num)
'''

'''
print(list)
index = list.index("shubham")# give index of shubham
print(index)

'''

'''
list.extend([7,8,9,0,7,8,7,7])
print(list)
num_7 = list.count(7)
print(num_7)

'''

'''
list = [-2,9,4,2,7,11]
'''

'''
list.sort()
print(list)
list.reverse()
print(list)
'''

'''
copy_list = list
print(copy_list)
copy_list.append(9)
print(copy_list)
print(list)
'''

'''
copy_list = list.copy()
print(copy_list)
copy_list.append(9)
print(copy_list)
print(list)

'''

'''
list.clear()
print(list)

'''

#Q->Print positive and negative elements of an List?

'''
list = [1,-9,0,-2,4,-3,-5,0]

print("postive number")
for num in list:
    if num > 0:
        print(num)

print("neagtive number")
for num in list:
    if num < 0:
        print(num)   

print("zero in list")
for num in list:
    if num == 0:
        print(num)  
'''                    

#Q->Mean of List elements?

'''

list = [0,0,10,30,-10]
sum = sum(list)
mean = sum/len(list)
print(mean)

'''

#Q->Find the greatest element and print its index too?

'''
list = [-1,4,2,9,3,0]
max = max(list)
index = list.index(max)
print(index,max)
'''

#Q->Find the second greatest element?

'''
list = [0,8,9,7,-3,-5]
list.sort()
print(list[len(list)-2])
'''

'''
list = [0,8,9,7,-3,-5]
list_2 = [0,8,9,7,-3,-5]
print(list == list_2)

'''





#2 Tuple

'''
tuple = (9,0,7,11.9,0,-5,"shubham")
print(tuple)

print(tuple[1])

#tuple[1] = "hacker" -> this is wrong.the main diffrence bettween tuple and list
print(tuple)
'''


#3.Set
