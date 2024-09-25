'''
Largest Element in an array using python
Here, in this page we will discuss the program to find the largest element in an array using python we are given with an array elements and we need to print the largest among the given elements. 
We discuss different methods to find the largest element using python programing language.

'''

# 1 bubble sort

'''
array =[int(i) for i in input().split()]
for i in range(0 ,len(array)):
    for j in range(0 ,len(array)-1):
        if array[j]>array[j+1]:
            # c=array[j]
            # array[j]=array[j+1]
            # array[j+1] =c
            array[j] , array[j+1] = array[j+1] ,array[j]
print(array)
print(array[-1]) # to print largest element


'''

# 2 Selection sort

'''

def selectionsort(array):
    for i in range(len(array)-1):
        minimumindex =i
        for j in range(i+1 ,len(array)):
            if array[j]<array[minimumindex]:
                minimumindex =j
        if i!=minimumindex:
            array[i] ,array[minimumindex] = array[minimumindex], array[i]

array = [45,20,50,15,10,15]
selectionsort(array)
print(array)
print(array[-1]) # to print largest element

'''




