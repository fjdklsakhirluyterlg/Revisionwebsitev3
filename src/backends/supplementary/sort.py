from .fisheryates import randomise

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def bogosort(array):
    while not arraySorted(array):
        randomise(array)
    

def arraySortedOrNot(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True

    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])

def arraySorted(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return True
 
    for i in range(1, n):
        if (arr[i-1] > arr[i]):
            return False
    return True

array = [9, 8, 3, 4, 5, 2]
bogosort(array)
print(array)