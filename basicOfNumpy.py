import numpy as np

'''
arrayOne = {1,2,3,4,5}
arrayTwo = [0,1,2]
print(arrayOne);
print(arrayTwo);

#list

list = [1,0]

'''

'''

python_list = [-1,0,1]; #with comma
print(python_list);



numpy_array = np.array([0,1,0]);#without comma effecient way of use memory
print(numpy_array)

'''

#2D array

'''
arr_2d = np.array([
    [1,0,1],
    [2,0,3]
])

print(arr_2d)


arr_3d = np.array([
    [
        [0,0,1],
        [0,1,2]
    ],
    [
        [-1,8,9],
        [0,-3,1]
    ]
])

print(arr_3d)
'''

'''
zeros_array = np.zeros((3))
print(zeros_array)

zeros_array_3d = np.zeros((3,2,2))
print(zeros_array_3d)
'''

'''
ones_array = np.ones((2,2))
print(ones_array)

'''

'''
filled_array = np.full((2,2),(7))
print(filled_array)

'''

'''
arr = np.arange(0,12,3)
print(arr)

'''

'''
identity_matrix = np.eye((4))
print(identity_matrix)
'''

'''
identity_matrix = np.eye((4))
print(identity_matrix.shape)
print(identity_matrix.ndim)
print(identity_matrix.size)
print(identity_matrix.dtype)
print(identity_matrix.astype(int))
'''

'''
arr = np.array([10,2,3])
print(arr + 5)
print(arr - 5)
print(arr*5)
print(arr // 5)
print(arr ** 2)
'''

'''
arr = np.array([0,7,3])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.max(arr))
print(np.min(arr))

'''

'''
numpy_arr = np.array([0,1,2,1,2,1,3,4,0])
print(numpy_arr[1])
print(numpy_arr[-1])

numpy_2d_arr = np.array([
    [0,1],
    [-2,7]
])

print(numpy_2d_arr[1,0])
'''

'''
arr = np.array([1,2,3,4,5,6,7,8,9,0])
print(arr[0:11:2])
print(arr[:11])
print(arr[::3])
print(arr[::-1])#reverse ordering

print(arr[[2,4]])

identity_matrix = np.eye(4,5)
# identity_matrix = np.identity(4)

print(identity_matrix)
print(identity_matrix[[1,3]])

'''

'''
numpy_arr = np.array([1,0,2,8,9,3,4,6])
print((numpy_arr>3).astype(int))
print(numpy_arr[numpy_arr > 3])
'''

'''
numpy_arr = np.array([0,1,2,3,4,5,8,9])
print(numpy_arr.size)
reshaped_arr = numpy_arr.reshape(2,2,2)
print(reshaped_arr)
print(numpy_arr)
print(numpy_arr.reshape(2,4))
print(numpy_arr)

'''

'''
arr = np.array([np.arange(0,9,1).reshape((3,3))])
print(arr)
print(arr.ravel())
print(arr.flatten())

'''

'''
arr = np.array([1,2,3,9])
print(arr)
modified_arr = np.insert(arr,1,7,axis = 0)
print(modified_arr)

arr_2d = np.array([
    [1,2],
    [3,4]
])
print(arr_2d)
new_arr_2d = np.insert(arr_2d,2,[0,0],axis = 1)
print(new_arr_2d)
new_arr_1d = np.append(arr,[0,1,2])
print(new_arr_1d)
'''

'''
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
arr_3 =np.concatenate((arr_1,arr_2),axis = 0)
print(arr_3)

'''

'''
arr_1 = np.array([1,2,3])
arr_2 = np.delete(arr_1,1)
print(arr_2)

arr_2d = np.array([
    [1,2],[5,6]
])

arr_new_2d = np.delete(arr_2d,0,axis = 1)
print(arr_new_2d)

'''

'''
arr_1 = np.array([1,1])
arr_2 = np.array([2,2])
print(np.vstack((arr_1,arr_2)))
print(np.hstack((arr_1,arr_2)))

'''

'''
arr = np.array([1,2,3,4,5,6])
print(np.split(arr,2))

'''

'''
arr = np.arange(1,13)
reshaped = arr.reshape(3,2,2)
print(reshaped)

'''

'''
arr = np.array([0,9,1,3,8])
print(np.sort(arr))

'''

'''

Write a NumPy program to:

Create an array of numbers from 1 to 20
Replace all even numbers with -1
'''


'''
arr = np.arange(1, 21)

for i in range(20):
    if arr[i] % 2 == 0:
        arr[i] = -1

print(arr)

'''


'''
arr = np.arange(1,21)
arr[arr % 2 == 0] = -1;
print(arr)

'''


'''
arr = np.array([10, 25, 40, 5, 30])

# Step 1: Find maximum
max_val = np.max(arr)

# Step 2: Remove max element
filtered = arr[arr != max_val]

# Step 3: Find second largest
second_max = np.max(filtered)

# Step 4: Find index
index = np.where(arr == second_max)[0][0]

print("Array:", arr)
print("Second Largest Element:", second_max)
print("Index:", index)

'''

















