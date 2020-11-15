#!/bin/python
import pytest
from w9_1 import BinTree

@pytest.fixture(Tree,listok)
def adding_Tree(Tree,listok):
    for el in listok:
        Tree.add(el)
    return Tree


@pytest.mark.parametrize('list_for_add',([1,7,3,9,11],
                                                [0,10,8,0,101,19],
                                                [i for i in range(10)]))
def test_BinTree(list_for_add,adding_Tree):
    Tree_example = BinTree(list_for_add[0])
    Tree_example = adding_Tree(Tree_example,list_for_add[1::])
    assert Tree_example.PrintTree == sorted(list_for_add)




