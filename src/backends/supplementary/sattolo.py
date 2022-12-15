from random import randrange

def sattolo_cycle(items) -> None:
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i) 
        items[j], items[i] = items[i], items[j]

list = [1, 2, 3, 5, 6, 7, 9, 2]
sattolo_cycle(list)
print(list)