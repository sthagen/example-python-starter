"""CLI interface for starter."""
from typing import List, Union

import starter.starter as impl


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the processing."""
    code, messages = impl.process(argv)
    for message in messages:
        print(message)
    return code
