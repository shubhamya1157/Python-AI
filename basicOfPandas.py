import pandas as pd


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

''

