#!/usr/bin/env python3
"""0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
