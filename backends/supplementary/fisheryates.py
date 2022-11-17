from random import randint
def randomize (arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        j = randint(0,i+1)
        arr[i],arr[j] = arr[j],arr[i]
    return arr