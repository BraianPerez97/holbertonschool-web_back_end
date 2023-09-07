#!/usr/bin/env python3
"""Pagination in python"""


def index_range(self, page: int, page_size: int) -> tuple:
        """
        Returns tuple of start and end indexes 
        for given page and page size.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index