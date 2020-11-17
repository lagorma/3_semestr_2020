#!/bin/python
import pytest
from w8_6 import get_combinations
from itertools import combinations

@pytest.mark.parametrize('s,n,answer',(['cat',2,['a', 'c', 't', 'ac', 'at', 'ct']],['fedcba',1,['a', 'b', 'c', 'd', 'e', 'f']],['qwerty',0,[]]))
def test_get_combinations(s,n,answer):
    assert get_combinations(s,n) == answer
