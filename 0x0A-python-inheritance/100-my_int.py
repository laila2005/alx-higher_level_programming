#!/usr/bin/python3
"""
this module represents a
class that inherits from int.
"""


class MyInt(int):
    """MyInt is a rebel class that inherits from int."""

    def __eq__(self, other):
        """Inverts the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality operator."""
        return super().__eq__(other)
