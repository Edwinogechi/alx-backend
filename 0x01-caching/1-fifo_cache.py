#!/usr/bin/python3
"""Defines a FIFOCache class that inherits from BaseCaching."""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A First-In-First-Out (FIFO) caching implementation."""

    def __init__(self):
        """Initialize the FIFOCache."""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Store the item in the cache using the FIFO strategy."""
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """Retrieve the value associated with the given key from the cache."""
        return self.cache_data.get(key)
