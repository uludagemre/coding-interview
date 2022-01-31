from typing import *


def str2arr(s: Text, type_: Callable = int) -> list:
    return [type_(x) for x in s.split(",")]