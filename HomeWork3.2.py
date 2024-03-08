import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()

    return numbers
    

print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))