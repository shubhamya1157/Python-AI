'''
Write a Python program using Matplotlib to plot a simple line graph showing the
relationship between years (2015–2024) and sales revenue (in millions). Label the axes and
provide a title for the plot.
a)Modify the previous line plot to include grid lines, customize the line style to a dashed red
line, and add a legend. 
'''

import matplotlib.pyplot as plt 
import pandas as pd

'''
# line graph
year = []
sales_revenue = []

for num in range(2015,2025):
    year.append(num)

for sales in range(2,12):
    sales_revenue.append(sales**2)

plt.plot(year,sales_revenue,linestyle = "--",color = "red",label = 'revenue')
plt.xlabel("years")
plt.ylabel("sales revenue")
plt.grid(True)
plt.legend()
plt.show()


'''

'''
Create a line plot comparing the sales revenue of two different companies (Company A and
Company B) over the years 2015–2024. Use different colors and markers for each line and
include a legend.

'''

'''
year = []
company_a = []
company_b = []

for num in range(2015,2025):
    year.append(num)


for data in range(2,12):
    company_a.append(data)

for data in range(1,11):
    company_b.append(data)

plt.plot(year,company_a,marker = "o",label = "company b revenue")
plt.plot(year,company_b,color = "red",marker = "s",label = "company a revenue")

plt.legend(True)

plt.show()

'''
'''


data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [200, 250, 300, 280, 350]
}

df = pd.DataFrame(data)
plt.plot(df["Year"],df["Sales"],marker = "o")
plt.grid(True)
plt.show()

'''

'''


Task:
Plot sales vs year
Add markers
Add grid

'''


'''
Given Data:

Task:
Filter students with marks > 50
Plot bar chart only for filtered data
Add labels

'''


'''
data = {
    'Name': ['A','B','C','D','E'],
    'Marks': [90,40,75,30,85]
}

df = pd.DataFrame(data)

# Filter students with marks > 50
filtered_df = df[df["Marks"] > 50]

# Plot bar chart
plt.bar(filtered_df["Name"], filtered_df["Marks"], label="Marks")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")

plt.legend()
plt.show()

print(filtered_df,filtered_df["Marks"])

'''
