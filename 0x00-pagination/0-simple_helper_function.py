#!/usr/bin/env python3
"""A utility function for calculating start and end indices"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing a start index and an end index"""

    return (page * page_size - page_size, page * page_size)
