"""Implementation of starter."""
from typing import List, Tuple, Union


def is_integer(text: str) -> bool:
    """Fantastic findings."""
    try:
        int(text)
        return True
    except ValueError:
        return False


def process(argv: Union[List[str], None] = None) -> Tuple[int, List[str]]:
    """Process all arguments."""
    argv = [] if argv is None else argv
    messages: List[str] = []
    if argv:
        if not is_integer(argv[0]):
            return 1, messages
        messages.append('integer')

    messages.append('starter')
    return 0, messages
