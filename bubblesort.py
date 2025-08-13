def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
arr=[4,6,8,0,8,4,50]
p_arr=bubblesort(arr)
print(bubblesort(arr))