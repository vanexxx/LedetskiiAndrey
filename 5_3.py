#Задача А
try:
    func()

except ValueError:
    print("ValueError")

except TypeError:
    print("TypeError")

except SystemError:
    print("SystemError")

else:
    print("No Exceptions")

#Задача B
func(None, "0")

#Задача C
class Error:
    def __repr__(self):
        return


func(Error())

#Задача D
def only_positive_even_sum(a: int, b: int) -> int:
    if not isinstance(b, int) or not isinstance(a, int):
        raise TypeError

    if a < 0 or b < 0 or a % 2 or b % 2:
        raise ValueError

    return a + b

#Задача E
def merge(*iterables) -> list:
    for iterable in iterables:
        try:
            _ = iter(iterable)
        except Exception:
            raise StopIteration

    d_type = type(iterables[0][0])

    type_error = False
    value_error = False

    for iterable in iterables:
        if not all(map(lambda x: isinstance(x, d_type), iterable)):
            type_error = True
            break
        if list(iterable) != sorted(iterable):
            value_error = True

    if type_error:
        raise TypeError
    if value_error:
        raise ValueError

    sorted_list = []
    left, right = iterables
    l_index = r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            sorted_list.append(left[l_index])
            l_index += 1
        else:
            sorted_list.append(right[r_index])
            r_index += 1

    sorted_list += left[l_index:]
    sorted_list += right[r_index:]

    return sorted_list

#Задача F
class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a: int | float, b: int | float, c: int | float) -> tuple:
    if not all(isinstance(num, (int, float)) for num in (a, b, c)):
        raise TypeError

    if not a:
        if not b:
            if not c:
                raise InfiniteSolutionsError
            raise NoSolutionsError
        root = -c / b
        return (root,)

    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        bigger_root = (-b + discriminant**0.5) / (2 * a)
        smaller_root = (-b - discriminant**0.5) / (2 * a)
        return smaller_root, bigger_root

    raise NoSolutionsError

#Задача G
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError

    for char in name:
        char_index = ord(char)
        if not (1040 <= char_index <= 1105 or char_index == 1025):
            raise CyrillicError

    if name != name.capitalize():
        raise CapitalError

    return name

#Задача H
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError

    for char in name:
        char_index = ord(char)
        if not (
            48 <= char_index <= 57  # 0-9
            or 65 <= char_index <= 90  # A-Z
            or 97 <= char_index <= 122  # a-z
            or char_index == 95  # _
        ):
            raise BadCharacterError

    if name[0].isdigit():
        raise StartsWithDigitError

    return name

#Задача I
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def all_cyrillic(word: str) -> bool:
    for char in word:
        char_index = ord(char)
        if not (1040 <= char_index <= 1105 or char_index == 1025):
            return False
    return True


# fmt: off
def all_chars_good(word: str) -> bool:
    if not word:
        return False
    for char in word:
        char_index = ord(char)
        if not (
            48 <= char_index <= 57      # 0-9
            or 65 <= char_index <= 90   # A-Z
            or 97 <= char_index <= 122  # a-z
            or char_index == 95         # _
        ):
            return False
    return True
# fmt: on


def user_validation(**details) -> dict:
    blueprint = ("last_name", "first_name", "username")

    if tuple(details.keys()) != blueprint:
        raise KeyError

    for key, value in details.items():
        if not isinstance(value, str):
            raise TypeError

        if key == "username":
            if not all_chars_good(value):
                raise BadCharacterError

            if value[0].isdigit():
                raise StartsWithDigitError

        if key in {"last_name", "first_name"}:
            if not all_cyrillic(value):
                raise CyrillicError

            if value != value.capitalize():
                raise CapitalError

    return details

#Задача J
import string
from hashlib import sha256
from typing import Callable


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    p_word: str,
    min_length: int = 8,
    possible_chars: str = None,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    if not isinstance(p_word, str):
        raise TypeError

    if not possible_chars:
        possible_chars = set(string.ascii_letters + string.digits)

    if len(p_word) < min_length:
        raise MinLengthError

    if not all(map(lambda x: x in possible_chars, p_word)):
        raise PossibleCharError

    if not any(map(at_least_one, p_word)):
        raise NeedCharError

    return sha256(p_word.encode("utf-8")).hexdigest()

#Задача K

#Задача L

#Задача M

#Задача N

#Задача O

#Задача P
