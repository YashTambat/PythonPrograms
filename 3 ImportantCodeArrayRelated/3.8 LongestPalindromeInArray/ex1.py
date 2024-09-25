''''
Find the Longest Palindrome in an Array using Python

'''


'''

arr = [1, 232, 5545455, 909090, 161]
output: 5545455

'''


array =[int(i) for  i in input().split()]
palindrome_Array =[]
for i in array:
    x = str(i)[::-1]
    if int(x)==i:
        palindrome_Array.append(i)
print(max(palindrome_Array))


   
    