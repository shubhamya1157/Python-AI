import numpy as np

import pandas as pd


'''
Create a DataFrame with:

Name, Age, Marks, City

👉 Tasks:

Display students with Marks > 70 AND Age < 20
Display students from a specific city (user input)
Find students whose name contains letter "a"
Exclude students with marks < 40

'''


'''
data = {
    "Name" : ["alapha","beta","gama","delta"],
    "Age" : [17,18,19,22],
    "Marks" : [100,89,56,78],
    "city" : ["mumbai","banglor","hydrabad","delhi"]
}

df = pd.DataFrame(data)

print(df[(df["Marks"] > 70) & (df["Age"] < 20)])
print(df["city"])
print(df[df["city"] == "mumbai"])
rdf["Name"].str.contains("a")

'''

'''

A college stores attendance data:

Name	Subject	Attendance (%)
A	Math	85
B	Sci	60
C	Math	72
D	Eng	40
E	Sci	90
Tasks using Pandas:

a) Create DataFrame
b) Find students with attendance < 75%
c) Find subject-wise average attendance
d) Count students per subject
e) Add column "Status" (Eligible if ≥75 else Not Eligible)
f) Sort by attendance

'''

'''
data = {
    "Name" : ["A","B","C","D","E"],
    "subject" : ["Math","Sci","Math","Eng","Sci"],
    "Attendence" :[85,60,72,40,90]
}

df = pd.DataFrame(data)

print(df)

print(df[df["Attendence"] < 75])

'''

'''

👉 Dataset contains:

Duplicate students
Missing marks

Perform:

Remove duplicates
Fill missing marks with average
Reset index

'''


'''

# Create dataset
data = {
    "student_id": [2, 2, 2, 2, 2, 5, 5, 2],
    "name": ["Aman", "Riya", "Riya", "Karan", "Neha", "Simran", "Simran", "Raj"],
    "marks": [85, None, None, 78, 92, None, None, 88]
}

df = pd.DataFrame(data)

# 1. Remove duplicates based on student_id
# df = df.drop_duplicates(subset='student_id')
modified_df = df.drop_duplicates(subset = "student_id")
print(modified_df)

modified2_df = df.drop_duplicates(subset = "name")
print(modified2_df)


# 2. Fill missing marks with average
average_marks = df['marks'].mean()
df['marks'] = df['marks'].fillna(average_marks)

# 3. Add grade column
def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    else:
        return 'C'

df['grade'] = df['marks'].apply(assign_grade)

# 4. Sort by marks (descending)
df = df.sort_values(by='marks', ascending=False)

# 5. Reset index
df = df.reset_index(drop=True)

# 6. Print final dataset
print(df)

'''


data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Aman", "Riya", "Karan", "Neha"],
    "Subject": ["Math", "Math", "Math", "Math", "Science", "Science", "Science", "Science"],
    "Marks": [85, 90, 78, 92, 88, 76, 80, 95]
}

df = pd.DataFrame(data)

'''
print(df.groupby("Subject").groups)
print(df.groupby("Subject").sum())
print(df.groupby("Subject").max())
print(df.groupby("Subject").min())
print(df.groupby("Subject")["Marks"].sum())

'''

# topper = df.loc[df.groupby('Subject')['Marks'].idxmax()]

# print("Topper of each subject:")
# print(topper)



# avergage marks of each subject 

'''
avg_marks = df.groupby("Subject")["Marks"].mean()
print(avg_marks)

'''


'''
data = {
    "Roll No": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["Aman", "Riya", "Karan", "Neha", "Simran", "Raj", "Pooja", "Arjun"],
    "Class": ["10A", "10A", "10A", "10A", "10B", "10B", "10B", "10B"],
    "Marks": [85, 35, 78, 92, 60, 30, 75, 88],
    "Attendance": [80, 70, 90, 95, 65, 85, 72, 98],
    "Section": ["A", "A", "A", "A", "B", "B", "B", "B"]
}

df = pd.DataFrame(data)


'''
# df["Eligibility"] = "Eligible"
# df.loc[df["Attendance"] < 75, "Eligibility"] = "Not Eligible"
# print(df)

'''


'''

'''

df["FinalResult"] = "Pass"

df.loc[df["Marks"] < 40 , "FinalResult "] = "fail"
df.loc[df["Attendance"] < 75 ,"FinalResult"] = "fail"

print(df)

'''



'''
data = {
    "Student_ID": [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
    "Name": ["A", "B", "C", "D", "E", "E", "F", "G", "H", "I"],
    "Subject": ["Math", "Math", "Math", "Science", "Science", "Science", "Math", "Science", "Math", "Science"],
    "Marks": [95, 105, -10, 88, np.nan, np.nan, 76, 150, 45, 60]
}

df = pd.DataFrame(data)

# print(df)

df.loc[df["Marks"] < 0, "Marks"] = np.nan

df.dropna(inplace = True)
print(df)
# df.fillna(df["Marks"].mean(), inplace = True)
# print(df)

# df.drop_duplicates()
# print(df)

'''





