'''
/*
Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
*/
'''

def alternate_posneg(arr):
    n=len(arr)
    j=-1
    temp=0
    for i in range(n):
        if arr[i]<0:
            j+=1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp

    print("The sorted negative and positive array is: ", arr)

    neg=0
    pos=j+1
    while(neg<pos and pos<n and arr[neg]<0):
        temp=arr[neg]
        arr[neg]=arr[pos]
        arr[pos]=temp
        pos+=1
        neg+=2
    print("The sorted array after alternating positive and negative numbers is:", arr)

arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print("The given array is: ", arr)
alternate_posneg(arr)