'''
Maximum product of sub-array in Python
Here, in this page we will discuss the program to find the maximum product of sub-array in python programming language. We are given with an array and need to return the maximum value of the product of the sub-array.


Example
Input : arr = [ 1, -2, -3, 0, 7, -8, -2 ]
Output : Maximum product sub-array is 112

'''

def maxSubarrayProduct(arr , n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
       
        # traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]
         
        # updating the result for (n-1)th index.
        result = max(result, mul)
     
    return result
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))