#!/usr/bin/env python3
""" Type Checking  """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zoom Array """
    z_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return z_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
