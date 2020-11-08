#!/bin/python
from itertools import permutations
from w8_5 import get_permutations
import pytest

@pytest.mark.parametrize('word,l,answer',(['cat',2,["ac", "at", "ca", "ct", "ta", "tc"]],['fedcba',1,['a', 'b', 'c', 'd', 'e', 'f']],['qwerty',0,['']]))
def test_get_permutations(word,l,answer):
    assert get_permutations(word,l) == answer
