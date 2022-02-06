from typing import *


def str2list(s: Text, type_: Callable = int) -> list:
    return [type_(x) for x in s.strip("[]").split(",")]