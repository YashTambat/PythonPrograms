'''

Example
Input : 2 3
Output : 8

'''
a =2
b =3
print(pow(a,b))



# method 2: using iteration
'''
num, power = 3, 2
output = 1
for i in range(power):
  output*=num
print(output)

'''

#method 3: recursion


'''

def powerOFnumber(num , power):
    if power==0:
        return 1
    return num* powerOFnumber(num, power-1) 

num ,power=3 ,2
print(f"Power of {num} is: ",powerOFnumber(num,power))


'''