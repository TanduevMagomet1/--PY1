import random
digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

characters_in_the_password = uppercase + lowercase + digits

def generate_random_password(n: int) -> list[int]:
    return "".join(random.sample(characters_in_the_password, n))


generated_random_password = generate_random_password(10)
print(generated_random_password)