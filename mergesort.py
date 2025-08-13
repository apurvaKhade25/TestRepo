def mergesort(arr):
    if len(arr)<+1:
        return arr
    
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    leftsort=mergesort(left)
    rightsort=mergesort(right)

    return merge(leftsort,rightsort)

def merge(left,right)