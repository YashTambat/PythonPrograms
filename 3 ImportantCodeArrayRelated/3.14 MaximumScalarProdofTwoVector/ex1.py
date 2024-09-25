'''
Maximum Scalar Product of two Vectors in Python
Here, in this page we will discuss the program to find the maximum scalar product of two vectors in python programming language.
Scalar product is also known as dot product. We are given with two vectors and need to print the maximum dot product obtained.

Example
Input :arr1[4] = [10, 30, 40, 20]
        arr2[4] = [2, 4, 5, 1]
Output : 370
Explanation : 10*1 + 20*2 + 30*4 + 40*5 = 370


Sort the first and second array in ascending order.
Declare a variable say product = 0.
Run a loop from index 0 to n
Set product += (arrr1[i]*arr2[i])
After complete iteration print product.
'''


arr1 = [10, 30, 40, 20]
arr2 = [2, 4, 5, 1]
arr1.sort()
arr2.sort()
product = 0
for i in range(len(arr1)):
    product+=arr1[i]*arr2[i]

print(product) # op : 370