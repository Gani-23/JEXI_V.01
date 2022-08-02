def arrsub(arr):
    sum = 0
    length = len(arr)
    for i in range(0,length):
        sum = pow((arr[i]-arr[length]),2)
    return sum

arr = [1,3,5,2,10]
arrsub(arr)