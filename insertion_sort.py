#insertion sort
def insertion(A,ascend=1):
    if ascend:
        for i in range(0,len(A)):
            key=A[i]
            j = i-1
            while j>=0 and A[j]>key:
                A[j+1]=A[j]
                j-=1
            A[j+1]=key
    else:
        for i in range(0,len(A)):
            key=A[i]
            j = i-1
            while j>=0 and A[j]<key:
                A[j+1]=A[j]
                j-=1
            A[j+1]=key
    return(A)



test_array=[25,13,188,24,1,2,9,56]
print test_array
print insertion(test_array)
print insertion(test_array,0)
