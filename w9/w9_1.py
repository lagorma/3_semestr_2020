#!/bin/python
class BinTree:

    def update_tree(self):
        self.dfs_iter = iter(self.DFS(self))

    def __init__(self, name):

        self.left = None
        self.right = None
        self.name = name
        self.update_tree()

    def add(self, name):
        if self.name:
            if name < self.name:
                if self.left is None:
                    self.left = BinTree(name)
                else:
                    self.left.add(name)
            elif name > self.name:
                if self.right is None:
                    self.right = BinTree(name)
                else:
                    self.right.add(name)
        else:
            self.name = name
        self.update_tree()

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.name),
        if self.right:
            self.right.PrintTree()

    def DFS(self, root):
        res = []
        if root:
            res = self.DFS(root.left)
            res.append(root.name)
            res = res + self.DFS(root.right)
        return res

    def __iter__(self):
            return self

    def __next__(self):
            return next(self.dfs_iter)
