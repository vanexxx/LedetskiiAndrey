#Задача А
from typing import List


def make_list(length: int, value: int = 0) -> List[int]:
    return [value] * length

#Задача B
from typing import List, Tuple, Union


def make_matrix(
    size: Union[Tuple[int], int], value: Union[int, None] = None
) -> List[List[int]]:
    if not value:
        value = 0
    if isinstance(size, int):
        size = (size, size)

    return [[value] * size[0] for _ in range(size[1])]

#Задача C
def gcd(*numbers) -> int:
    if len(numbers) < 2:
        return numbers[0] if numbers else None

    a = numbers[0]

    for b in numbers[1:]:
        while b:
            a, b = b, a % b

    return a

#Задача D
from typing import Union


def month(number: Union[int, str], lang: str = "ru") -> str:
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
def to_string(*data, sep: str = " ", end: str = "\n") -> str:
    n = len(data)
    result = []

    for i in range(n):
        element = str(data[i])

        if i == n - 1:
            sep = end

        result.append(element)
        result.append(sep)

    return "".join(result)

#Задача F
from threading import Lock
from typing import Dict

IN_STOK_LOCK = Lock()
RECIPIES = {
    "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
    "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
    "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
    "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
}


def check_ingredients(ingredients: Dict[str, int]) -> bool:
    """Проверка достаточности ингредиентов для напитка"""
    with IN_STOK_LOCK:
        return all(
            in_stock.get(ingredient, 0) >= quantity
            for ingredient, quantity in ingredients.items()
        )


def update_stock(ingredients: Dict[str, int]) -> None:
    """Обновление ингредиентов в остатках"""
    with IN_STOK_LOCK:
        for ingredient, quantity in ingredients.items():
            in_stock[ingredient] -= quantity


def order(*preferences) -> str:
    for drink in preferences:
        ingredients = RECIPIES.get(drink, None)

        if ingredients and check_ingredients(ingredients):
            update_stock(ingredients)
            return drink

    return "К сожалению, не можем предложить Вам напиток"

#Задача G
from typing import Tuple


def enter_results(*pairs) -> Tuple[float]:
    global results

    if "results" in globals():
        results.extend(list(pairs))
    else:
        results = list(pairs)


def get_sum() -> Tuple[float]:
    global results
    global total

    total = list(results[:2])

    for i in range(2, len(results), 2):
        total[i % 2] += results[i]
        total[(i + 1) % 2] += results[i + 1]

    return round(total[0], 2), round(total[1], 2)


def get_average() -> Tuple[float]:
    global results
    global total

    length = len(results) // 2

    return tuple(round(total[i] / length, 2) for i in range(2))

#Задача H
lambda x: (len(x), x.lower())

#Задача I
lambda x: not sum(map(int, str(x))) % 2

#Задача J
def secret_replace(text: str, **replaces) -> str:
    repeats = {}
    encoded = []

    for char in text:
        if char in replaces:
            if char not in repeats:
                repeats[char] = 0
            elif repeats[char] < len(replaces[char]) - 1:
                repeats[char] += 1
            else:
                repeats[char] = 0

            encoded_char_index = repeats[char]
            encoded_char = replaces[char][encoded_char_index]
            encoded.append(encoded_char)

        else:
            encoded.append(char)

    return "".join(encoded)