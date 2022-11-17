from random import randint
def randomise (arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        j = randint(0,i+1)
        arr[i],arr[j] = arr[j],arr[i]
    return arr

array = [1, 2, 7, 4, 3, 9, 8, 6]
randomise(array)