def search(arr, n , x):

    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1

arr = [0,1,2,3,4,5]
x = 3
n = len(arr)

search(arr,n,x)

    




