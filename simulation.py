
'''
import random
import matplotlib.pyplot as plt
import math

N = 5000
inside_x, inside_y = [], []
outside_x, outside_y = [], []

inside = 0

for _ in range(N):
    x = random.random()
    y = random.random()

    if x*x + y*y <= 1:
        inside += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

pi_est = 4 * inside / N
error = abs(math.pi - pi_est)

print("Estimated π:", pi_est)
print("Actual π:", math.pi)
print("Error:", error)

# Plot
plt.scatter(inside_x, inside_y)
plt.scatter(outside_x, outside_y)
plt.title("Monte Carlo π Estimation")
plt.show()

'''


import numpy as np
import random 
import matplotlib.pyplot as plt 


'''

l = []

for i in range(100):
    x = random.randint(1,10)
    l.append(x)


arr = np.array(l)
print(arr)

# brr = arr.reshape(10,10)
# print(brr)
# values,count = np.unique(arr,return_counts = True)

# print(values,count)

# plt.plot(values,count)
# plt.scatter(values,count)
# plt.bar(values,count)

# plt.show()

'''

'''

arr = np.random.randint(1,10,size = (10,10))
print(arr)
brr = arr.reshape(1,100)
print(brr)

'''
