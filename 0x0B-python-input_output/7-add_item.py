#!/usr/bin/python3
<<<<<<< HEAD
"""7-add_item.py
script that adds all arguments to a Python list, and then save them to a file:
"""


import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.isfile(filename):
    json_file = load_from_json_file(filename)
    json_list = json_file + sys.argv[1:]
    save_to_json_file(json_list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
=======
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
