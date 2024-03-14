import typing  # служебные аннотации типов
import collections.abc  # Callable, Sequence, Mapping

x: int = 5  # аннотация типа переменной


class Counter:
    x: int = 5  # аннотация типа поля класса

    # аннотация типов аргументов
    def __init__(self: Counter, x: int):
        self.x = x

    # аннотация типов аргументов
    # и типа возвращаемого значения
    def count(self: Counter) -> int:
        self.x += 1
        return self.x
