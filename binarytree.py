#!/usr/bin/env python3
from collections import deque

class BinaryTree(object):
    '''
    A binary tree.
    '''
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)


    def set(self, key, value):
        '''
        Adds the given key=value pair to the tree.
        '''
        #TODO
        if self.root:
            self._set(key, value, self.root)
        else:
            self.root = Node(None, key, value)

    def _set(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.left != None:
                self._set(key, value, currentNode.left)
            else:
                currentNode.left = Node(currentNode, key, value)
        else:
            if currentNode.right != None:
                self._set(key, value, currentNode.right)
            else:
                currentNode.right = Node(currentNode, key, value)


    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        #TODO
        if self.root:
            temp = self._get(key, self.root)
            if temp:
                return temp.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.left)
        else:
            return self._get(key, currentNode.right)


    def remove(self, key):
        '''
        Removes the given key from the tree.
        Returns silently if the key does not exist.
        '''
        #TODO        
        nodeToRemove = self._get(key, self.root)
        if nodeToRemove:
            self._remove(nodeToRemove)
        else:
            raise KeyError('Key not in tree. Please try again.')

    def _remove(self, currentNode):
        if not (currentNode.left or currentNode.right): #leaf
            if currentNode.parent.left == currentNode:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.left and currentNode.right: #has both children
            succ = currentNode._findNext()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value
        else: #one child
            if currentNode.left:
                if currentNode.parent and currentNode.parent.left == currentNode:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.parent and currentNode.parent.right == currentNode:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:
                    currentNode._replace_node(currentNode.left.left, currentNode.left.right)
            else:
                if currentNode.parent and currentNode.parent.left == currentNode:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.parent and currentNode.parent.right == currentNode:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode._replace_node(currentNode.right.left, currentNode.right.right)


    def walk_dfs_inorder(self):
        '''
        An iterator that walks the tree in DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        if self.root is None:
            return
        if self.root.left is not None:
            yield from self._walk_dfs_inorder(self.root.left)
        yield (self.root.key, self.root.value)
        if self.root.right is not None:
            yield from self._walk_dfs_inorder(self.root.right)

    def _walk_dfs_inorder(self, currentNode):
        if currentNode is None:
            return
        if currentNode.left is not None:
            yield from self._walk_dfs_inorder(currentNode.left)
        yield (currentNode.key, currentNode.value)
        if currentNode.right is not None:
            yield from self._walk_dfs_inorder(currentNode.right)


    def walk_dfs_preorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in preorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        if self.root is None:
            return
        yield (self.root.key, self.root.value)
        if self.root.left is not None:
            yield from self._walk_dfs_preorder(self.root.left)
        if self.root.right is not None:
            yield from self._walk_dfs_preorder(self.root.right) 

    def _walk_dfs_preorder(self, currentNode):
        if currentNode is None:
            return
        yield (currentNode.key, currentNode.value)
        if currentNode.left is not None:
            yield from self._walk_dfs_preorder(currentNode.left)
        if currentNode.right is not None:
            yield from self._walk_dfs_preorder(currentNode.right)        


    def walk_dfs_postorder(self, node=None, level=0):
        '''
        An iterator that walks the tree in inorder DFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        # "yield from walk_*()" when recursing
        if self.root is None:
            return
        if self.root.left is not None:
            yield from self._walk_dfs_postorder(self.root.left)
        if self.root.right is not None:
            yield from self._walk_dfs_postorder(self.root.right)
        yield (self.root.key, self.root.value)

    def _walk_dfs_postorder(self, currentNode):
        if currentNode is None:
            return
        if currentNode.left is not None:
            yield from self._walk_dfs_postorder(currentNode.left)
        if currentNode.right is not None:
            yield from self._walk_dfs_postorder(currentNode.right)
        yield (currentNode.key, currentNode.value)


    def walk_bfs(self):
        '''
        An iterator that walks the tree in BFS fashion.
        Yields (key, value) for each node in the tree.
        '''
        #TODO
        # "yield (key, value)" for current node
        queue = []
        if self.root:
            queue.append(self.root)
        while queue:
            current = queue.pop(0)
            yield (current.key, current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    ##################################################
    ###   Helper methods


    def _replace_node(self, oldnode, newnode):
        '''
        Internal method to remove a node from its parent
        '''
        #TODO: feel free to use or remove this method
        self.left = oldnode
        self.right = newnode
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


class Node(object):
    '''
    A node in a binary tree.
    '''
    def __init__(self, parent, key, value):
        '''Creates a linked list.'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        result = []
        def recurse(node, prefix1, side, prefix2):
            if node is None:
                return
            result.append(prefix1 + node.key + side)
            if node.right is not None:
                recurse(node.left, prefix2 + '\u251c\u2500\u2500 ', ' \u2c96', prefix2 + '\u2502   ')
            else:
                recurse(node.left, prefix2 + '\u2514\u2500\u2500 ', ' \u2c96', prefix2 + '    ')
            recurse(node.right, prefix2 + '\u2514\u2500\u2500 ', ' \u1fe5', prefix2 + '    ')
        recurse(self, '', '', '')
        return '\n'.join(result)

    def _findNext(self):
        '''
        Internal method to find a node by key.
        Returns (parent, node).
        '''
        #TODO: feel free to use or remove this method
        nextNode = None
        if self.right:
            nextNode = self.right.findMin()
        else:
            if self.parent:
                if self.left:
                    nextNode = self.parent
                else:
                    self.parent.right = None
                    nextNode = self.parent._findNext()
                    self.parent.right = self
        return nextNode

    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current

    def spliceOut(self):
        if not (self.right or self.left):
            if self.parent and self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.right or self.left:
            if self.left:
                if self.parent and self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.parent and self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent