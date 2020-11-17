#!/bin/python
import pytest
from itertools import groupby
from w8_8 import compress_string

@pytest.mark.parametrize('word,answer',(['1222311',[(1, 1), (3, 2), (1, 3), (2, 1)]],['aaabccccddaa',[(3, 'a'), (1, 'b'), (4, 'c'), (2, 'd'), (2, 'a')]],['',[]]))
def test_compress_string(word,answer):
    assert compress_string(word) == answer
