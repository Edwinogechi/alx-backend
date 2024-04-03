#!/usr/bin/python3
"""Defines a LIFOCache class that inherits from BaseCaching."""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A Last-In-First-Out (LIFO) caching implementation."""

    def __init__(self):
        """Initialize the LIFOCache."""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Store the item in the cache using the LIFO strategy."""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key from the cache."""
        return self.cache_data.get(key)
