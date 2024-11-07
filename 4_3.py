#Задача А
def recursive_sum(*numbers) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum(*numbers[1:])

#Задача B
def recursive_digit_sum(number: int) -> int:
    number = str(number)
    if len(number) == 1:
        return int(number[0])
    return int(number[0]) + recursive_digit_sum(number[1:])

#Задача C
def make_equation(*numbers) -> str:
    if len(numbers) == 1:
        return f"{numbers[0]}"
    return f"({make_equation(*numbers[:-1])}) * x + {numbers[-1]}"

#Задача D
def answer(func: callable) -> str:

    def wrapper(*args, **kwargs) -> str:
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper

#Задача E
from typing import Callable, List, Optional, TypeVar

T = TypeVar("T")


def result_accumulator(func: Callable[..., T]) -> Optional[List[T]]:
    def wrapper(
        *args, method: str = "accumulate", **kwargs
    ) -> Optional[List[T]]:
        if not hasattr(wrapper, "results"):
            wrapper.results: List[T] = []

        wrapper.results.append(func(*args, **kwargs))

        if method == "drop":
            accumulated_results = wrapper.results[:]
            wrapper.results.clear()
            return accumulated_results
        return None

    return wrapper

#Задача F
def merge_sort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_part = numbers[:mid]
    right_part = numbers[mid:]

    return merge(merge_sort(left_part), merge_sort(right_part))


def merge(left: list, right: list) -> list:
    merged = []
    left_index = right_index = 0
    l_length, r_length = len(left), len(right)

    while left_index < l_length and right_index < r_length:
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

#Задача G
from typing import Callable, TypeVar

T = TypeVar("T")


def same_type(func: Callable[..., T]) -> Callable[..., str | T]:
    def wrapper(*args: T, **kwargs) -> str | T:
        data_type = type(args[0])
        for data in args[1:]:
            if not isinstance(data, data_type):
                print("Обнаружены различные типы данных")
                return "Fail"
        else:
            return func(*args, **kwargs)

    return wrapper

#Задача H
def fibonacci(num: int):
    if not num:
        return
    if num < 2:
        yield 0
    else:
        a, b = 0, 1
        yield a
        yield b
        for _ in range(num - 2):
            a, b = b, a + b
            yield b

#Задача I
def cycle(iterable):
    index = 0
    while True:
        yield iterable[index]
        index += 1
        if index == len(iterable):
            index = 0

#Задача J
def make_linear(iterable: list) -> list:
    answer = []

    for i in iterable:
        if isinstance(i, list):
            answer.extend(make_linear(i))
        else:
            answer.append(i)

    return answer