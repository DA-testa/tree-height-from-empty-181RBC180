import numpy as np

def find_depth(node, tree):
    if node == -1:
        return 0
    else:
        return 1 + find_depth(tree[node], tree)

def main():
    input()
    tree = np.array(input().split(), dtype=int)
    index = int(np.where(tree == -1)[0])
    # print(index)
    depth = find_depth(0, tree)
    print(depth)

main()
