'''
Step 1: Read file and create dictionary
students = {}

with open("students.csv", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students[name] = int(marks)

max_student = ""
max_marks = 0

for name in students:
    if students[name] > max_marks:
        max_marks = students[name]
        max_student = name



# Step 3: Calculate average marks
total_marks = sum(students.values())
average_marks = total_marks / len(students)


# Step 4: Count students above average
count = 0

for marks in students.values():
    if marks > average_marks:
        count = count + 1


# Step 5: Print results
print("Student Data:", students)
print("Highest Marks Student:", max_student, "→", max_marks)
print("Average Marks:", average_marks)
print("Students Above Average:", count)

'''


'''
Read the file
Convert data into a list of dictionaries like:

'''

'''
data = []

with open("sales_data.txt","r") as file:
    for line in file:
        
        data.append({
            "name":name,
            "cateory":category,
            "sales": int(sales)
        })

# print(data)
# print(data[0])

totel_sales = sum(d["sales"] for d in data)
# print(totel_sales)

avg_salary = totel_sales/len(data)
# print(avg_salary)

'''

'''
file students.csv contains:

name,marks,attendance
A,78,80
B,45,75
C,90,95
D,NaN,85
E,67,NaN
F,120,88

Tasks

Load using pandas
Handle missing values:
replace with column mean
Remove invalid data:
marks > 100
Add new column:
"grade":
≥80 → A
50–79 → B
<50 → C
Find:
topper
average attendance of grade A students
Save cleaned dataset to cleaned.csv

'''

import pandas as pd 

'''

df = pd.read_csv("file.csv")# Converted into DataFrame

# print(df)
# print(df.info())
# df = df.dropna()

df["marks"] = df["marks"].fillna(df["marks"].mean())
df["attendance"] =df["attendance"].fillna(df["attendance"].mean())

# print(df)

df = df[df["marks"] < 100]

# print(df)

df["grade"] = 'B'
df.loc[df["marks"] >= 80,"grade"] = 'A'
df.loc[df["marks"] < 50 ,"grade"] = 'C'

# print(df)

# print("Topper of the class is:",max(df["marks"]))

# print(df[df["marks"] == max(df["marks"])]["name"])
# print(df[["name","attendance"]])


# print((df[df["grade"] == "A"]["attendance"].mean()))

# df.to_csv("cleaned.csv")
df.to_csv("cleaned.csv",index = False)

'''


'''

Problem

A file orders.txt:

101,Electronics,5000
102,Clothing,2000
103,Electronics,7000
104,Clothing,3000
105,Electronics,10000

Tasks

Read file
Convert into list of dictionaries
Convert into JSON


'''
