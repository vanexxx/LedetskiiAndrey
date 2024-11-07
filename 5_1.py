#Задача А
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

#Задача B
class Point:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    def move(self, dx: float | int, dy: float | int) -> None:
        self.x += dx
        self.y += dy

    def length(self, other: "Point") -> float | int:
        distance_squared = (other.x - self.x) ** 2 + (other.y - self.y) ** 2
        return round(distance_squared**0.5, 2)

#Задача C
class RedButton:
    def __init__(self) -> None:
        self.counter = 0

    def click(self) -> None:
        print("Тревога!")
        self.counter += 1

    def count(self) -> int:
        return self.counter

#Задача D
class Programmer:
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        self.position_salary = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.bucks_per_hour = self.position_salary[self.position]
        self.hours = 0
        self.salary = 0

    def work(self, hours: int) -> None:
        self.hours += hours
        self.salary += self.bucks_per_hour * hours

    def rise(self) -> None:
        match self.bucks_per_hour:
            case 10:
                self.position = "Middle"
                self.bucks_per_hour = self.position_salary[self.position]
            case 15:
                self.position = "Senior"
                self.bucks_per_hour = self.position_salary[self.position]
            case _:
                self.bucks_per_hour += 1

    def info(self) -> str:
        info = f"{self.name} {self.hours}ч. {self.salary}тгр."
        return info

#Задача E
class Rectangle:
    def __init__(self, point_one: tuple, point_two: tuple) -> None:
        self.x_one, self.y_one = point_one
        self.x_two, self.y_two = point_two

        self.height = abs(self.y_one - self.y_two)
        self.width = abs(self.x_one - self.x_two)

    def perimeter(self) -> float:
        calc_perimeter = (self.height + self.width) * 2

        return round(calc_perimeter, 2)

    def area(self) -> float:
        calc_area = self.height * self.width

        return round(calc_area, 2)

#Задача F
class Rectangle:
    def __init__(self, point_one: tuple, point_two: tuple) -> None:
        self.x_one, self.y_one = point_one
        self.x_two, self.y_two = point_two

        self.height = abs(self.y_one - self.y_two)
        self.width = abs(self.x_one - self.x_two)

    def perimeter(self) -> float:
        calc_perimeter = (self.height + self.width) * 2

        return round(calc_perimeter, 2)

    def area(self) -> float:
        calc_area = self.height * self.width

        return round(calc_area, 2)

    def get_pos(self) -> tuple:
        x = min(self.x_one, self.x_two)
        y = max(self.y_one, self.y_two)

        return round(x, 2), round(y, 2)

    def get_size(self) -> tuple:
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx: float | int, dy: float | int) -> None:
        self.x_one += dx
        self.x_two += dx
        self.y_one += dy
        self.y_two += dy

    def resize(self, width: float | int, height: float | int) -> None:
        self.width = width
        self.height = height

        x, y = self.get_pos()

        self.x_one = x
        self.y_one = y
        self.x_two = x + self.width
        self.y_two = y - self.height

#Задача G
class Rectangle:
    def __init__(self, point_one: tuple, point_two: tuple) -> None:
        self.x_one, self.y_one = point_one
        self.x_two, self.y_two = point_two

        self.height = abs(self.y_one - self.y_two)
        self.width = abs(self.x_one - self.x_two)

    def perimeter(self) -> float:
        calc_perimeter = (self.height + self.width) * 2

        return round(calc_perimeter, 2)

    def area(self) -> float:
        calc_area = self.height * self.width

        return round(calc_area, 2)

    def get_pos(self) -> tuple:
        x = min(self.x_one, self.x_two)
        y = max(self.y_one, self.y_two)

        return round(x, 2), round(y, 2)

    def get_size(self) -> tuple:
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx: float | int, dy: float | int) -> None:
        self.x_one += dx
        self.x_two += dx
        self.y_one += dy
        self.y_two += dy

    def resize(self, width: float | int, height: float | int) -> None:
        self.width = width
        self.height = height

    def turn(self) -> None:
        center_x, center_y = self._get_center()

        new_x_one = center_x - (self.y_one - center_y)
        new_y_one = center_y + self.x_one - center_x

        new_x_two = center_x - (self.y_two - center_y)
        new_y_two = center_y + self.x_two - center_x

        self.x_one, self.y_one = new_x_one, new_y_one
        self.x_two, self.y_two = new_x_two, new_y_two

        self.width, self.height = self.height, self.width

    def scale(self, factor: float | int) -> None:
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)

        center_x, center_y = self._get_center()

        self.x_one = (self.x_one - center_x) * factor + center_x
        self.y_one = (self.y_one - center_y) * factor + center_y

        self.x_two = (self.x_two - center_x) * factor + center_x
        self.y_two = (self.y_two - center_y) * factor + center_y

    def _get_center(self) -> tuple:
        center_x = (self.x_one + self.x_two) / 2
        center_y = (self.y_one + self.y_two) / 2

        return center_x, center_y

#Задача H
class Cell:
    def __init__(self, state: str) -> None:
        self.state = state

    def status(self) -> str:
        return self.state


class Checkers:
    def __init__(self) -> None:
        self.board = {}
        row_pieces_even = {
            "1": "W",
            "2": "X",
            "3": "W",
            "4": "X",
            "5": "X",
            "6": "X",
            "7": "B",
            "8": "X",
        }
        row_pieces_odd = {
            "1": "X",
            "2": "W",
            "3": "X",
            "4": "X",
            "5": "X",
            "6": "B",
            "7": "X",
            "8": "B",
        }

        for row in "87654321":
            for index, col in enumerate("ABCDEFGH"):
                if index % 2 == 0:
                    state = row_pieces_even[row]
                else:
                    state = row_pieces_odd[row]

                position = col + row
                self.board[position] = Cell(state)

    def move(self, current: str, move_to: str) -> None:
        checker = self.board[current]
        self.board[move_to] = checker
        self.board[current] = Cell("X")

    def get_cell(self, position: str) -> Cell:
        return self.board[position]

#Задача I
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue: list[T] = []

    def push(self, item: T) -> None:
        self.queue.append(item)

    def pop(self) -> T:
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

#Задача J
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.stack: list[T] = []

    def push(self, item: T) -> None:
        self.stack.append(item)

    def pop(self) -> T:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0