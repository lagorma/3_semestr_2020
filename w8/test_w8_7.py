#!/bin/python
from itertools import combinations_with_replacement
import pytest
from w8_7 import get_combinations_with_r

@pytest.mark.parametrize('word,l,answer',(['cat',2,["aa", "ac", "at", "cc", "ct", "tt"]],['fedcba',1,['a', 'b', 'c', 'd', 'e', 'f']],['qwerty',0,['']]))
def test_get_combinations_with_r(word,l,answer):
    assert get_combinations_with_r(word,l) == answer
