#!/usr/bin/env python3
"""2-lifo_cache
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache
    """

    def __init__(self):
        """init
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """get
        """
        return self.cache_data.get(key, None)
