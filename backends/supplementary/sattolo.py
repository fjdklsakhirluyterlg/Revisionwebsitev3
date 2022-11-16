from random import randrange

def sattolo_cycle(items) -> None:
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i) 
        items[j], items[i] = items[i], items[j]

print(sattolo_cycle([2, 3, 4, 5, 1, 4]))