import random

def generate_random_id():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(16):
        result += characters[random.randint(0, charactersLength)]
    
    return result