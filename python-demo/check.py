from string import ascii_letters, digits
from random import choices, randint

characters = ascii_letters + digits

CORRECT_PASSWORD = "".join(choices(characters, k=randint(10, 15)))
LENGTH = len(CORRECT_PASSWORD)

assert all(c in characters for c in CORRECT_PASSWORD)


def check_password_vulnerable(password: str) -> bool:
    """
    Checks if the password is correct.

    This is intentionally made to be vulnerable to show how a side channel timing attack could be made
    """
    if len(password) != LENGTH:
        return False
    for a, b in zip(password, CORRECT_PASSWORD):
        if a != b:
            return False
    return True


def check_password_safe(password: str) -> bool:
    return password == CORRECT_PASSWORD
