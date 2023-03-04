# python3
import sys
import threading
import numpy as np

def find_depth(node, tree):
    if node == -1:
        return 0
    else:
        return 1 + find_depth(tree[node], tree)

def main():
    input()
    tree = np.array(input().split(), dtype=int)
    depth = find_depth(0, tree)
    print(depth)

main()
