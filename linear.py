def linear(arr,target):
    n=len(arr)
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
n=int(input("enter no of elements: "))
arr=[]
# arr=[3,4,5,6,8,9,0]
# target=9
for i in range(n):
    num=int(input(f"enter {i+1} element: "))
    arr.append(num)
target=int(input("enter element to be searched: "))
result=linear(arr,target)

if result==-1:
    print("target not foung")
else:
    print(f"target found at {result}")

