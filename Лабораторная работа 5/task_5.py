import random
from string import ascii_letters, digits


def generate_random_password(n: int) -> list[int]:
    characters_in_the_password = ascii_letters + digits
    return "".join(random.sample(characters_in_the_password, n))


generated_random_password = generate_random_password(10)
print(generated_random_password)
# Ответ