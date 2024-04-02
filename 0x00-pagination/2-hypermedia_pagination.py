#!/usr/bin/env python3
'''Description: This script implements a method called get_page.
    It takes two integer arguments: page (default value 1) and
    page_size (default value 10).
'''
import csv
from math import ceil
from typing import List


index_range = __import__('0-simple_helper_function').index_range


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
        ''' Retrieve a page of the dataset.. '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' Return dict of pagination data.
            Dict key/value pairs consist of the following:
                page_size - length of the returned dataset page
                page - current page number
                data - dataset page eq to return from prev task
                next_page - number of next page if there exists one
                prev_page - number of previous page if there exists one
                total_pages - total number of pages in the dataset as int'''
        page_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }
