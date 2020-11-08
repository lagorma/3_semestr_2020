#!/bin/python
import pytest
from itertools import starmap
from w8_9 import poisk
from w8_9 import maximize

@pytest.mark.parametrize("lists,m,answer",(  [[[5, 4],[7, 8, 9],[5, 7, 8, 9, 10]],1000,206],
                                             [[[25,19,0,3],[1,2,3],[99,0,10,100]],100,34],
                                             [[[-10,0,1],[0,-100],[10,-1]],10000,101]))
def test_maximize(lists,m,answer):
    assert maximize(lists,m) == answer
