#!/usr/bin/python3
""" Base Caching.
"""


class BaseCaching():
    """ BaseCaching.
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze.
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ put.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ get.
        """
        raise NotImplementedError("get must be implemented in your cache class")
