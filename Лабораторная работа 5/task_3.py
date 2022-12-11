import random


def get_unique_list_numbers() -> list[int]:
    # list comprehension не используется, так как неизвестно сколько раз нужно вызвать randint, так как он может выдавать одинаковые числа, а по условию в списке они должны быть уникальные
    random_unique_numbers = []
    while len(random_unique_numbers) < 15:
        random_unique_number = random.randint(-10, 10)
        if random_unique_number not in random_unique_numbers:
            random_unique_numbers.append(random_unique_number)
    return random_unique_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Ответ