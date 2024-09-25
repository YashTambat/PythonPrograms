'''
Finding Minimum scalar product of two vectors: 

arr1 = 20 , 10 , 40 ,60 ,30
arr2 =20 , 10 ,50 ,40 ,30

sort arr1 in ASC
sort arr2  in DESC
product =0

Run a loop from index 0 to 4  and set product+= arr1[i]*arr2[i]
product = 10*50 + 20*40 + 30*30+ 40*20 + 60*10 = 3600

'''

arr1 = [20 , 10 , 40 ,60 ,30]
arr2 =[20 , 10 ,50 ,40 ,30]
arr1.sort()
arr2.sort(reverse=True)
product =0
for i in range(5):
    product += arr1[i]*arr2[i]
print(product)

