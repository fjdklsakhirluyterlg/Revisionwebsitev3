def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


arr1 = [9, 3, 4, 2, 1, 8]
arr2 = ["amin", "boo", "see", "go", "zi", "lift", "hhh", "nee"]
print(quick_sort(arr1)) 