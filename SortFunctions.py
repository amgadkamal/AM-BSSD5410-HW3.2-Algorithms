def minIndex(a, i, j):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)
def recurSelectionSort(a, n, index = 0):

    if index == n:
        return -1
    k = minIndex(a, index, n- 1)

    if k != index:
        a[k], a[index] = a[index], a[k]
    recurSelectionSort(a, n, index + 1)


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)



def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h



def binarySearchSub(arr,l,r,x):
    mid = 0
    while l <= r:
        mid = l + (r-l) // 2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r= mid -1
    return mid

def selectionSort(A,compare):
 for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if compare(A[min_idx],A[j]):
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

 def mergeSort(arr):
     if len(arr) > 1:
         mid = len(arr) // 2  # Finding the mid of the array
         L = arr[:mid]  # Dividing the array elements
         R = arr[mid:]  # into 2 halves

         mergeSort(L)  # Sorting the first half
         mergeSort(R)  # Sorting the second half

         i = j = k = 0

         # Copy data to temp arrays L[] and R[]
         while i < len(L) and j < len(R):
             if L[i] < R[j]:
                 arr[k] = L[i]
                 i += 1
             else:
                 arr[k] = R[j]
                 j += 1
             k += 1

         # Checking if any element was left
         while i < len(L):
             arr[k] = L[i]
             i += 1
             k += 1

         while j < len(R):
             arr[k] = R[j]
             j += 1
             k += 1



