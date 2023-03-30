#!/usr/bin/env python3
""" Complex Strict types"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    params: a string k and an int OR float v as arguments
    returns a tuple.
    """

    return (k, v**2)
