
Project 0x01: Caching
Overview
Project 0x01, titled "Caching", is a software project aimed at implementing caching mechanisms in various programming languages. Caching is a critical technique in computer science and software engineering, which involves storing frequently accessed data in a temporary storage area, known as a cache, to expedite the retrieval of data and improve system performance.

This project explores different caching strategies, algorithms, and implementations across multiple programming languages to understand their strengths, weaknesses, and applicability in various scenarios.

Features
Implementation of various caching strategies:
Least Recently Used (LRU)
First-In-First-Out (FIFO)
Least Frequently Used (LFU)
Random Replacement
etc.
Support for different data structures for caching:
Arrays
Linked Lists
Hash Tables
Trees
etc.
Evaluation and comparison of caching strategies based on:
Performance metrics (e.g., hit rate, miss rate)
Memory overhead
Implementation complexity
Scalability
Documentation and examples for each implemented caching strategy.
Comprehensive testing suite to ensure the correctness and performance of caching implementations.
Installation
This section will provide instructions for installing and setting up the project environment. It may involve installing dependencies, setting up virtual environments, or any other necessary steps to get the project up and running.

Usage
Here, users will find guidelines on how to utilize the caching implementations provided by the project. It will include code examples, API documentation, and usage scenarios for each caching strategy.

Contributing
Contributions to the project are welcome! Whether it's fixing bugs, adding new features, improving documentation, or suggesting new caching strategies, your contributions are valuable. Please refer to the contribution guidelines for more information on how to contribute to the project.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes. See the LICENSE file for more details.

Acknowledgments
This project is inspired by the importance of caching in computer science and software engineering.
We extend our gratitude to the open-source community for their contributions to caching algorithms and implementations, which served as a valuable resource for this project.
Contact
For any inquiries, feedback, or suggestions regarding the project, please contact project@example.com.




Tasks
0. Basic dictionary
mandatory
Create a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

1. FIFO caching
mandatory
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

2. LIFO Caching
mandatory
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

3. LRU Caching
mandatory
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

4. MRU Caching
mandatory
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

5. LFU Caching
#advanced
Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
