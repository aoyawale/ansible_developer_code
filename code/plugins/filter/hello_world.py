"""A hello-world filter plugin in ansible_dev.my_code."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=C0103


def _hello_world(name):
    """Returns Hello message."""
    return "Hello, " + name


class FilterModule:
    """filter plugin."""

    def filters(self):
        """filter plugin."""
        return {"hello_world": _hello_world}
