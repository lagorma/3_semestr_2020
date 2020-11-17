#!/bin/python
import pytest
from w8_3 import copy_zip
from w8_3 import copy_map
from w8_3 import copy_enumerate


@pytest.mark.parametrize('a,b,c',[['hello',[1,2,3],(0,0,0,5)],[[0],[1,2,3],'mew']])
def test_copy_zip(a,b,c):
    assert list(zip(a, b, c)) == list(copy_zip(a, b, c))


@pytest.mark.parametrize('a,b',[(int,['1','2','3']),(float, ['1','2.5','3.0'])])
def test_copy_map(a,b):
    assert list(copy_map(a,b)) == list(map(a,b))

@pytest.mark.parametrize('a',([1,2,3],('a','b','c'),('banana')))
def test_copy_enumarate(a):
    assert list(copy_enumerate(a)) == list (enumerate(a))

