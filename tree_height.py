def compute_height(n, parents):
    tree = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max(height(child) for child in tree[node])

    return height(root)

n = input()
parents = list(map(int, input().split()))
print(compute_height(int(n), parents))
