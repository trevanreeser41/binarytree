#!/usr/bin/env python3
from binarytree import BinaryTree
import sys



#
#                                c
#                                |
#                +---------------+---------------+
#                |                               |
#                a                               h
#        +-------+                       +-------+-------+
#        |                               |               |
#        b                               e               j
#                                        |               |
#                                    +---+---+       +---+---+
#                                    |       |       |       |
#                                    d       f       i       k
#                                            +
#                                            |
#                                            g
#

def main():
    tree = BinaryTree()
    tree.set('c', 'C')
    tree.set('h', 'H')
    tree.set('a', 'A')
    tree.set('e', 'E')
    tree.set('f', 'F')
    tree.set('d', 'D')
    tree.set('b', 'B')
    tree.set('k', 'K')
    tree.set('j', 'J')
    tree.set('i', 'I')
    tree.set('g', 'G')
    tree.set('l', 'L')

    print('Lookups:')
    print(tree.get('f'))
    print(tree.get('b'))
    print(tree.get('i'))
    print()

    print('DFS preorder:')
    for key, value in tree.walk_dfs_preorder():
        print(key, value)
    print()

    print('DFS inorder:')
    for key, value in tree.walk_dfs_inorder():
        print(key, value)
    print()

    print('DFS postorder:')
    for key, value in tree.walk_dfs_postorder():
        print(key, value)
    print()

    print('BFS:')
    for key, value in tree.walk_bfs():
        print(key, value)
    print()

    print('Initial tree:')
    print(tree)
    print()

    print('Remove b:')
    tree.remove('b')
    print(tree)
    print()

    print('Remove f:')
    tree.remove('f')
    print(tree)
    print()

    print('Remove h:')
    tree.remove('h')
    print(tree)
    print()



if __name__ == '__main__':
    main()
