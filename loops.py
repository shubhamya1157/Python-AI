# For Loop for numbers

'''
for i in range(9):
    print(i)

'''

'''
for shubham in range(7):
    print(shubham)
'''

'''
for i in range(-7 ,0):
    print(i)
'''

'''
for i in range( 1 , 9 ,0):
    print(i)
'''

'''
for i in range( 1 , 9 ,1):
    print(i)
'''      
'''
for i in range( 1 , 9 ,2):
    print(i)
#output
    i
    i+2
    i+2+2
    i+2+2+2
    i+2+2+2 >= 9 (9 and greater then 9 is exclude) 
'''
'''
for i in range( 1 , 9 ,-2):
    print(i)
'''

'''
for i in range( 9 , 1 ,-2):
    print(i)
'''    

# Loops for strings

name  = "shubham"
'''
for i in range(len(name)):
    print(i)
    print(name[i])

'''

'''
for i in range( 1 ,len(name) ,2):
    print(i)
    print(name[i])
'''  

'''
for char in name:
    print(char)
'''

'''
for char in name:
    if char == "s":
        continue
    elif char == "a":
        break
    else:
        print(char)    
'''

'''
for i in range(len(name)-1,-1 ,-1):
    print(name[i],end="")        
'''


'''
mix = "shu!bh@m1157"
digit = 0
letter = 0
symbol = 0

for char in mix:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
         letter += 1
    else:
        symbol += 1

print("number of digit is:",digit)
print("number of letter is:",letter)
print("number of symbol is:",symbol )

'''



# While loop

'''
num = 1157
digit = 0

while num != 0 :
    digit = num % 10
    print(digit)
    num = int(num /10)
'''

'''
num = 1157

for char in str(num):
    print(char)   
'''