#!/usr/bin/env python3
"""
Простой генератор паролей
Генерирует случайные пароли с настраиваемой длиной
"""

import random
import string
import argparse
import sys


def generate_password(length=12):
    """
    Генерирует случайный пароль заданной длины
    
    Args:
        length (int): Длина пароля (по умолчанию 12)
    
    Returns:
        str: Сгенерированный пароль
    """
    # Используем буквы (прописные и строчные) и цифры
    characters = string.ascii_letters + string.digits
    
    # Проверяем минимальную длину
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    """Основная функция для работы из командной строки"""
    parser = argparse.ArgumentParser(
        description="Генератор безопасных случайных паролей",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python password_generator.py              # Пароль длиной 12 символов
  python password_generator.py -l 16        # Пароль длиной 16 символов
  python password_generator.py --length 8   # Пароль длиной 8 символов
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Длина пароля (по умолчанию: 12)'
    )
    
    args = parser.parse_args()
    
    try:
        password = generate_password(length=args.length)
        
        print(f"Сгенерированный пароль: {password}")
        print(f"Длина: {len(password)} символов")
        
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
