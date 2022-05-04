'''
Find the maximum element in an array
A=[1,4,9,16,25,36,48,56,64,5,0]
'''

def findMax(A):
    l = len(A)
    max=A[0]
    print("The max element in the array before findmax is first element which is :", max)
    print ("the length of the array is", l)
    for i in A:
        if i>max:
            max=i
    print("The max element in the array is: ", max)



A=[1,4,9,16,25,36,48,56,64,5,0]
print("The given array is: ", A)
findMax(A)