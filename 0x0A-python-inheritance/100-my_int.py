#!/usr/bin/python3
""" My  module
"""


class MyInt(int):
    """inverted == and != operators"""

    def __eq__(self, other):
        """Inverts equality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Inverts inequality"""
        return not super().__ne__(other)
