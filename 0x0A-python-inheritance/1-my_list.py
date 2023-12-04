#!/usr/bin/python3

"""Define class Mylist with inherited list."""


class MyList(list):
    """Custom list class."""
    def print_sorted(self):
        """Sorted printing in ascending order."""
        print(sorted(self))
