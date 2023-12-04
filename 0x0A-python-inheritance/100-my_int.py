#!/usr/bin/python3
"""Defines a Myint class"""


class MyInt(int):
    """inverts int operators == and !="""

    def __eq__(self, num):
        """inverts == to !="""
        return (self.real != num)

    def __ne__(self, num):
        """inverts != to =="""
        return (self.real == num)
