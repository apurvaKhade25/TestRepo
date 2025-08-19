def binary(arr, target):
    beg = 0
    end = len(arr) - 1
    
    while beg <= end:
        mid = (beg + end) // 2
        
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    
    return -1  

n=int(input("enter no of elements: "))
arr=[]
# arr=[3,4,5,6,8,9,0]
# target=9
for i in range(n):
    num=int(input(f"enter {i+1} element: "))
    arr.append(num)
target=int(input("enter element to be searched: "))
result=binary(arr,target)

if result==-1:
    print("target not found")

else:
    print(f"target found at {result}")
