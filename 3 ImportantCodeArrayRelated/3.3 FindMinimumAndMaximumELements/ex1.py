arr = [45, 20, 50, 15, 10]
mini = arr[0]
max = arr[0]


for i in range(len(arr)):
    if arr[i]<mini:
        mini = arr[i]
    if arr[i]>max:
        max=arr[i]

print(f"Minimum :{mini} and Maximum :{max}")






























