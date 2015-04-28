def nodeSort(A):
    quickSort(A, 0, len(A)-1)


def quickSort(A, lo, hi):
    if lo<hi:
        p = partition(A, lo, hi)

        quickSort(A, lo, p-1)
        quickSort(A, p+1, hi)


def partition(A, lo, hi):
    pivotValue = A[lo].f
 
    left = lo + 1
    right = hi
 
    done = False
    while not done:
        while left <= right and A[left].f <= pivotValue:
            left = left + 1
          
        while A[right].f >= pivotValue and right >= left:
            right = right -1
 
        if right < left:
            done = True
          
        else:
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
 
    temp = A[lo]
    A[lo] = A[right]
    A[right] = temp
 
    return right