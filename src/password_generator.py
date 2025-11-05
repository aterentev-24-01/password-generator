import random
import string

length = int(input("Введите длину пароля: ") or 12)
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Пароль: {password}")
