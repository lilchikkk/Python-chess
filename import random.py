import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Пример использования
if __name__ == "__main__":
    length = int(input("add length: "))
    print("generated password:", generate_password(length))
