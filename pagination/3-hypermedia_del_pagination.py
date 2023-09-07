#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Dict

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
        
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Method that returns a dictionary
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        data = self.get_page(page, page_size)
        total_length = len(self.dataset())
        total_pages = math.ceil(total_length / page_size)
        
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
    
        def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            """method that returns  dictionary of hyper_index"""

            assert index is not None and index < len(self.__indexed_dataset)
            
            data = list(self.__indexed_dataset.values())[index:index + page_size]

            next_index = index + page_size if index + page_size < len(self.__indexed_dataset) else None

            return {
                'index': index,
                'page_size': len(data),
                'data': data,
                'next_index': next_index
            }