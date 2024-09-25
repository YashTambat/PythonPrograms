
'''
ini_list = [10, 20, 30, 40, 40, 50, 50, 50]
output : [50, 50, 50, 40, 40, 10, 20, 30]
'''


array = [10, 20, 30, 40, 40, 50, 50, 50]
# sorting on bais of frequency of elements
result = sorted(array, key = array.count, reverse = True)
print(result)
