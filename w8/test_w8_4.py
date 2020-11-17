#!/bin/python
import pytest
from w8_4 import get_cartesian_product
from itertools import product

@pytest.mark.parametrize('a,b',(([1,2,3,4],['a','b','c','d']),(['b','a','n','a','n','a'],[0,1,2,3,4,5])))
def test_get_cartesian_product(a,b):
    assert get_cartesian_product(a,b) == list(product(a,b))
