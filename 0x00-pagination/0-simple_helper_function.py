#!/usr/bin/env python3
"""Pagination0.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
