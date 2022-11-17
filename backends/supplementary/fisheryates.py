from random import randint
def randomize (arr, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1,0,-1):
        # Pick a random index from 0 to i
        j = randint(0,i+1)
 
        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr