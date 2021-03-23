# -*- coding: utf-8 -*-

import pytest

from pandas_to_dll.dataframe_to_dll import dataframe_to_dll


@pytest.mark.parametrize(
    ("first", "second", "expected"), [(1, 2, 3), (2, 4, 6), (-2, -3, -5), (-5, 5, 0),]
)
def test_some_function(first, second, expected):
    """Example test with parametrization."""
    assert dataframe_to_dll(first, second) == expected
