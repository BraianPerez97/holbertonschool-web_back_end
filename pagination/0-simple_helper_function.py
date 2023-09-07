#!/usr/bin/env python3
"""Pagination in python"""


def index_range(page, page_size):
    """Function that returns a tuple size of two containing
    a start index and an end index corresponging
    to the range of indexes to return in a list of 
    pagination parameters"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index