# ========================================== 
# Day 07 - NumPy Fundamentals 
# Author: Sujaan Bhalla
# ========================================== 
print("Day 07 - NumPy Fundamentals")

import numpy as np 

# ========================================== 
# Creating Arrays
# ========================================== 
print("\n===== Creating Arrays =====")
arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# ==========================================
# Arange and Reshape
# ==========================================

arr = np.arange(12)
print(arr)

arr2d = arr.reshape(3,4)
print(arr2d)

arr3d = np.arange(24).reshape(2, 3, 4)
print(arr3d)

# ==========================================
# Array Properties
# ==========================================

print("Shape:", arr2d.shape)

print("Dimension:", arr2d.ndim)

print("Size:", arr2d.size)

print("Datatype:", arr2d.dtype)

# ==========================================
# Zeros
# ==========================================

arr = np.zeros(5)

print(arr)

arr = np.zeros((3, 4))

print(arr)

# ==========================================
# Ones
# ==========================================

arr = np.ones(5)

print(arr)

arr = np.ones((2, 3))

print(arr)

# ==========================================
# Full
# ==========================================

arr = np.full((3), 5)

print(arr)

arr = np.full((2, 3), 5)

print(arr)

# ==========================================
# Random
# ==========================================

arr = np.random.random(5)

print(arr)

arr = np.random.random((2, 3))

print(arr)

# ==========================================
# Arange
# ==========================================

arr = np.arange(5)

print(arr)

arr = np.arange(0, 10, 2)

print(arr)

# ==========================================
# Vector Matrix Tensor
# ==========================================

vector = np.array([1, 2, 3])

print(vector)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)

tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(tensor)

# ==========================================
# Flatten
# ==========================================

arr = np.arange(24).reshape(3, 2, 4)

flat = arr.flatten()

print(flat)

# ==========================================
# Ravel
# ==========================================

arr = np.arange(14).reshape(7, 2)

r = arr.ravel()

r[0] = 100

print(arr)

# ==========================================
# Transpose
# ==========================================

arr = np.arange(12).reshape(3, 4)

print(arr)

print(arr.T)

# ==========================================
# Sorting
# ==========================================

arr = np.array([10, 40, 30, 60, 90, 7, 5])

print(np.sort(arr))

# ==========================================
# Filtering
# ==========================================

arr = np.array([10, 20, 40, 6, 3, 4, 2])

filtered = arr[arr < 40]

print(filtered)

# ==========================================
# Fancy Indexing
# ==========================================

arr = np.array([10, 20, 3, 4, 90, 100])

print(arr[[0, 2]])

# ==========================================
# np.where
# ==========================================

arr = np.array([10, 3, 4, 80, 30, 40, 9])

result = np.where(arr > 40, arr + 2, arr - 2)

print(result)

# ==========================================
# Concatenate
# ==========================================

arr1 = np.array([10, 20, 30])

arr2 = np.array([1, 2, 3])

print(np.concatenate((arr1, arr2)))

# ==========================================
# Statistical Functions
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

print("Sum =", np.sum(arr))

print("Mean =", np.mean(arr))

print("Median =", np.median(arr))

print("Min =", np.min(arr))

print("Max =", np.max(arr))

print("Variance =", np.var(arr))

print("Standard Deviation =", np.std(arr))

# ==========================================
# Missing Values
# ==========================================

arr = np.array([1, 2, np.nan, 4])

print(np.isnan(arr))

# ==========================================
# End
# ==========================================

print("\nDay 07 Completed Successfully!")