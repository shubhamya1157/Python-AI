'''

Simulate rolling two dice 10,000 times.

Tasks

Compute probability of:
Sum = 7
Sum is even
At least one die shows 6
Find:
P(sum=7 | at least one 6)

'''


'''

import random

n = 10000

count_sum7 = 0
count_even = 0
count_one6 = 0
count_both = 0

for _ in range(n):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    s = d1 + d2
    
    if s == 7:
        count_sum7 += 1
        
    if s % 2 == 0:
        count_even += 1
        
    if d1 == 6 or d2 == 6:
        count_one6 += 1
        
    if s == 7 and (d1 == 6 or d2 == 6):
        count_both += 1


p_sum7 = count_sum7 / n
p_even = count_even / n
p_one6 = count_one6 / n


p_cond = count_both / count_one6

print(p_sum7, p_even, p_one6, p_cond)

'''


'''
Estimate value of π using random points.

 Tasks
Generate random (x, y) in range [0,1]
Count points inside circle
Estimate π

 Formula:

pi ≈ 4 * (points inside circle / total points)

'''

'''

import random

inside_point = 0;
n = 10000000

for i in range(n):
    x = random.random()
    y = random.random()

    if(x*x + y*y <= 1):
        inside_point += 1

pi =  4 * (inside_point/n)

print("Exproximate value of pi is:",pi);
     
'''
