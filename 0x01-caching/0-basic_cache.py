#!/usr/bin/env python3
"""base_caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """

    def put(self, key, item):
        """set
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get
        """
        return self.cache_data.get(key, None)
