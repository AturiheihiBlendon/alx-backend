#!/usr/bin/env python3
"""
helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple (startindex, endindex)
    """
    i_start = (page - 1) * page_size
    i_end = page * page_size
    return (i_start, i_end)
