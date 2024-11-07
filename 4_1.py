#Задача А
def print_hello(name: str) -> None:
    print(f"Hello, {name}!")

#Задача B
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

#Задача C
def number_length(number: int) -> int:
    if not number:
        return 1

    length = 0

    if number < 0:
        number = -number

    while number > 0:
        length += 1
        number //= 10

    return length

#Задача D
def month(number: int | str, lang: str) -> str:
    months = {
        "1": {"en": "January", "ru": "Январь"},
        "2": {"en": "February", "ru": "Февраль"},
        "3": {"en": "March", "ru": "Март"},
        "4": {"en": "April", "ru": "Апрель"},
        "5": {"en": "May", "ru": "Май"},
        "6": {"en": "June", "ru": "Июнь"},
        "7": {"en": "July", "ru": "Июль"},
        "8": {"en": "August", "ru": "Август"},
        "9": {"en": "September", "ru": "Сентябрь"},
        "10": {"en": "October", "ru": "Октябрь"},
        "11": {"en": "November", "ru": "Ноябрь"},
        "12": {"en": "December", "ru": "Декабрь"},
    }
    return months.get(str(number), {}).get(lang, "")

#Задача E
def split_numbers(numbers: str) -> tuple:
    return tuple(map(int, numbers.split()))

#Задача F
from typing import Set


def modern_print(phrase: str, cache: Set[str] = set()) -> None:
    if phrase in cache:
        return
    cache.add(phrase)
    print(phrase)

#Задача G
def can_eat(horsey: tuple, victim: tuple) -> bool:
    x1, y1 = horsey
    x2, y2 = victim
    hor = abs(x2 - x1) == 1 and abs(y2 - y1) == 2
    vert = abs(x2 - x1) == 2 and abs(y2 - y1) == 1
    return hor or vert

#Задача H
def is_palindrome(input_value) -> bool:
    if isinstance(input_value, (tuple, list)):
        input_value = list(map(lambda x: str(x).lower(), input_value))

    elif isinstance(input_value, str):
        input_value = "".join(map(lambda x: x.lower(), input_value.split()))

    else:
        input_value = str(input_value)

    return input_value == input_value[::-1]

#Задача I
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    elif n <= 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

#Задача J
def merge(left: tuple, right: tuple) -> tuple:
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return tuple(merged)