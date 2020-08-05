from timeit import timeit
from time import time
from string import ascii_letters, digits
from functools import lru_cache
from queue import PriorityQueue
from typing import Tuple, Optional, Iterator
from random import choices
from itertools import product

from check import check_password_vulnerable

characters = ascii_letters + digits


def find_length() -> int:

    NUMBER = 20000

    times = [
        timeit(lambda: check_password_vulnerable(" " * length), number=NUMBER)
        for length in range(21)
    ]

    return times.index(max(times))


def time_password(password: str, number: int = 40000) -> float:
    return timeit(lambda: check_password_vulnerable(password), number=number)


def pad(string: str, length: int) -> str:
    return string + " " * (length - len(string))


def brute_force(password: str, length: int) -> Optional[str]:
    for chars in product(characters, repeat=length - len(password)):
        new_password = password + "".join(chars)
        if check_password_vulnerable(new_password):
            return new_password
    return None


def find_password_iter(brute_force_limit: int = 3) -> Iterator[str]:

    length = find_length()

    q: PriorityQueue[Tuple[float, str]] = PriorityQueue()
    q.put((0.0, ""))

    while not q.empty():
        t, p = q.get()
        yield p

        if len(p) == length - brute_force_limit:
            # Brute force if there are not that many characters left
            i = 0
            for chars in product(characters, repeat=length - len(p)):
                np = p + "".join(chars)
                if i == 0:
                    yield np
                i = (i + 1) % 50
                if check_password_vulnerable(np):
                    yield np
                    return
        else:
            # Search using a depth first search
            for c in characters:
                np = p + c
                if check_password_vulnerable(np):
                    yield np
                    return
                q.put((-time_password(pad(np, length)), np))

    return


def find_password() -> str:

    for password in find_password_iter():
        pass

    return password


if __name__ == "__main__":

    from rich.console import Console
    import sys

    console = Console()
    console.show_cursor(False)
    for p in find_password_iter():
        console.control("\r\033[K")
        console.print(f"[red]{p}[/]", end="")
    if check_password_vulnerable(p):
        console.control("\r\033[K")
        console.print(f"[green]{p}[/]")
    console.show_cursor(True)
