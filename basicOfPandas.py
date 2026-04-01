import pandas as pd

import numpy as np


'''
df = pd.read_csv("student_dataset.csv")

'''

'''
data = {
    "name":["alpha","beta","gama","delta"],
    "age":[19,18,19,20],
    "class":[10,11,12,11],
    "city":["mumbai","hydrabad","delhi","jaipur"]
}

df = pd.DataFrame(data);
df.to_csv("output.csv",index = False)

print(df)

'''


'''
df = pd.read_csv("student_dataset.csv")
print(df)
print(df.to_string())
print(df.head(30))
print(df.tail(30))

'''

'''

print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)


print(df["Sleep_Hours"].to_string())
print(df[["Tutoring_Sessions","Final_Exam_Score"]].to_string())
print(df)
print(df[df["Attendance"] > 80].Hours_Studied)
print(df[(df["Attendance"] > 80) & (df["Hours_Studied"] > 20)])

'''



'''

data = {
    "name":["alpha","beta","gama","delta"],
    "age":[19,18,19,20],
    "class":[10,11,12,11],
    "city":["mumbai","hydrabad","delhi","jaipur"]
}

df = pd.DataFrame(data);

df["salary"] = [1000000,1000000,1500000,1230000]

print(df.to_string())

df.insert(0,"studentId",[1,2,3,4]);

print(df.to_string(index=False))

df.loc[1,"name"] = "tonybroooo"

print(df.to_string(index = False))

df["age"] = df["age"] * 0.5

print(df.to_string(index = False))

df.drop(columns = ["age"],inplace = True)

print(df.to_string(index = False))

# df.drop(columns = ["age","salary"],inplace = True)

'''

'''
print(df.isnull())

'''

'''
data = {
    "name":["alpha",None,"gama","delta"],
    "age":[19,18,19,None],
    "class":[10,11,12,11],
    "city" : [None,"hydrabad","delhi","jaipur"]
}

df = pd.DataFrame(data);
print(df.isnull())
print(df.isnull().sum())

'''

'''
df.dropna(axis = 0,inplace = True)
print(df)

'''

'''

df.dropna(axis = 1,inplace = True)
print(df)

'''

'''
df = df.fillna(df["class"].mean())
print(df)

'''


'''
df = pd.read_csv("student_dataset.csv")

print(df.shape)
print(df.shape[0])
print(df.shape[1])

'''

'''

list = [1157,"shubham","hacke",404.4,True]
print(list)
s = pd.Series(list , index = [0,1,2,3,4])
print(s)

'''

'''
Create a Series from the list [5, 10, 15, 20] with index ['a','b','c','d'].
Then:

Print values greater than 10
Multiply all elements by 2
'''


'''
list =  [5, 10, 15, 20] 
s = pd.Series(list,index = ['a','b','c','d'])
print(s[s > 10])

s = s * 2
print(s)
'''

'''

data = {
    "rollnumber" : [101,102,103,104,105,106,107,108],
    "name" : ["ram","mohan","rahul","rohan","rohit","mukesh","tony","alpha"],
    "class" : [10,10,10,11,12,11,11,10],
    "percentage" : [90,80,70,60,59,92,30,50],
    "division" : [1,1,1,1,2,1,3,2],
    "result" : ["pass","pass","pass","pass","pass","pass","fail","pass"]
}

df = pd.DataFrame(data)

'''

'''
print(df.tail(3))

print(df[df["name"] == "rahul"])

print(df[df["result"] == "fail"])

print(df[df["division"] == 1])

df_sorted = df.sort_values(by = "percentage",ascending = True)

print(df_sorted)

df_sorted_decress = df.sort_values(by = "percentage",ascending = False)

print(df_sorted_decress)

'''

''''
print([df["percentage"].max()])

print([df["percentage"].min()])


print(df.loc[df['percentage'].idxmin()])


print(df[df['percentage'] == df['percentage'].min()])

'''

'''
merge 
average
...

'''


'''

list = [1,2,3,4,5]

s1 = pd.Series(list)

s1[s1 % 2 == 0] ** 2

print(s1)

# s1 = s1 ** 2




s2 = pd.Series(list)

# s2 = s2 ** 3

'''

'''

Create a DataFrame with 8 students
Add column "Performance":
Excellent (>80)
Good (50–80)
Poor (<50)
Count students in each category

'''


'''

data = {
    "name" : ["alpha","beta","gama","delta","phi","chi","shi"],
    "percentange" : [89,99,10,40,30,70,49]
}

df = pd.DataFrame(data)

print("excellent:",df[df["percentange"] > 80])
# print("Good:", df[(df["percentage"] > 50) & (df["percentage"] <= 80)])
print("poor:",df[df["percentange"] <= 50 ])

print("excellent:",df[df["percentange"] > 80].count())
print("excellent:",len(df[df["percentange"] > 80]))
# print("Good:", df[(df["percentage"] > 50) & (df["percentage"] <= 80)].count())
print("poor:",df[df["percentange"] <= 50 ].count())

'''


'''
Create a NumPy array from 1 to 20
Reshape into 4×5 matrix
Extract:
First row
Last column
Flatten the array
Split into 2 equal parts

'''

'''
numpy_array = np.arange(1,21)
# print(numpy_array)

reshaped = numpy_array.reshape((4,5))

flat = reshaped.flatten()
print(flat)

# print(reshaped)

# print(reshaped[0])

# print(reshaped[0,1])

# split = np.array_split(flat,4)

print(split)

'''


'''
matrix = np.random.rand(3,3)
print(matrix)

matrix_2 = np.random.randint(1,10,size = (3,3))
print(matrix_2)

'''

'''
matrix = np.random.rand(12).reshape((3,4))
print(matrix)

'''


'''
matrix = np.linspace(1,10,12)
print(matrix)

matrix_2 = np.linspace(1,10,12).round()
print(matrix_2)

'''


'''
matrix_1 = np.random.randint(1,10,size =(3,3))
print(matrix_1)

matrix_2 = np.random.randint(4,20,size =(3,3))
print(matrix_2)

print(matrix_1 + matrix_2)
print(matrix_1 - matrix_2)

print(matrix_1 * matrix_2)
print(np.dot(matrix_1,matrix_2))
print(matrix_1 @ matrix_2)
print(matrix_1.T)
print(np.linalg.det(matrix_1))
print(np.linalg.inv(matrix_1))

'''

'''
Create DataFrame:

Employee ID, Name, Salary, Experience

👉 Perform:

Increase salary by:
20% if experience > 5
10% otherwise
Find highest paid employee
Sort employees by salary
Display employees earning above average salary

'''



'''

modified = df[df["experince"] > 5]
modified["salary"] = modified["salary"]* 1.2
# print(modified)
modified_2 = df[df["experince"] <= 5]
modified_2["salary"] = modified_2["salary"]* 1.1
# print(modified_2)

'''



'''
data = {
    "employId" : [101,102,103,104,105],
    "name" : ["alpha","beta","gama","delta","phi"],
    "salary" : [200000,120000,1560000,1210000,909000],
    "experince" : [4,5,10,9,7]
}

df = pd.DataFrame(data)

# Increase 20% where experience > 5
df.loc[df["experince"] > 5, "salary"] *= 1.2

# Increase 10% where experience <= 5
df.loc[df["experince"] <= 5, "salary"] *= 1.1

print(df)

'''

'''

Generate 10 random numbers using NumPy
Convert into DataFrame
Add columns:
Square
Log value (use NumPy)
Filter values greater than mean

'''

'''
numpy_array  = np.random.randint(1,12,size = (12))
print(numpy_array)

df = pd.DataFrame(numpy_array, columns=["number"])
print(df)

df["squre"] = df["number"] ** 2;

print(df)

'''

'''

Create a DataFrame:

Name, Subject, Marks

👉 Perform:

Group by Subject and find average marks
Find student with highest marks
Add column "Performance":
Excellent (>85)
Good (60–85)
Poor (<60)
Count students in each category


'''

'''

data = {
    "name" : ["alpha","beta","gama","delta","phi"],
    "sub" :["m","p","p","h","e"],
    "marks" : [99,89,34,78,56]
}

df = pd.DataFrame(data)

avg_marks = df["marks"].mean()

print(avg_marks)

# # Create column first
df["performance"] = ""

# Assign values based on conditions
df.loc[df["marks"] > 85, "performance"] = "excellent"

df.loc[(df["marks"] > 60) & (df["marks"] <= 85), "performance"] = "good"

df.loc[df["marks"] <= 60, "performance"] = "poor"

print(df)

'''

'''


Create array from 1 to 16
Reshape into 4×4
Extract:
Diagonal elements
First column
Flatten array

'''

'''
arr = np.linspace(1,11,16).reshape(4,4)
print(arr)

print(arr[ : 1])
flat = arr.flatten()
print(flat)


diag = np.diag(arr)

print(diag)
print(arr.T)
print(np.linalg.det(arr))
print(np.linalg.inv(arr))
print(np.trace(arr))

'''

