#!/usr/bin/env python3
"""
helper function
"""
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a list
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)
        if self.dataset() is None:
            return []
        return self.__dataset[index[0]: index[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple (startindex, endindex)
    """
    i_start = (page - 1) * page_size
    i_end = page * page_size
    return (i_start, i_end)
