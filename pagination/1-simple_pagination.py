#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List

class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Constructor method that initializes a cached dataset
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset property that loads data from CSV
        and stores in instance attribute.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Returns tuple of start and end indexes 
        for given page and page size.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the requested page of data
        using the page and page_size args.
        Validates inputs and indexes to dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_range = self.index_range(page, page_size)
        data = self.dataset()

        if page_range[0] >= len(data):
            return []
        else:
            return data[page_range[0]: page_range[1]]