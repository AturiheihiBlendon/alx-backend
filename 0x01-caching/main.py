#!/usr/bin/python3
# """ 0-main """
# BasicCache = __import__('0-basic_cache').BasicCache

# my_cache = BasicCache()
# my_cache.print_cache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))

""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

