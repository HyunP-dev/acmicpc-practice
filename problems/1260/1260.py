from collections import deque

import sys

sys.setrecursionlimit(10**4)


def dfs(tree, v):
    visited = [False] * (len(tree) + 1)
    result = []

    def loop(cur):
        visited[cur] = True
        result.append(cur)
        
        for node in tree[cur]:
            if not visited[node]:
                loop(node)

    loop(v)
    return result


def bfs(tree, v):
    visited = [False] * (len(tree) + 1)
    queue = deque([v])
    result = [v]
    visited[v] = True
    
    while queue:
        cur = queue.popleft()
        for node in tree[cur]:
            if not visited[node]:
                queue.append(node)
                result.append(node)
                visited[node] = True

    return result


tree: dict[int, list[int]] = {}

n, m, v = map(int, input().split())
for node in range(1, n + 1):
    tree[node] = []

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for node in tree:
    tree[node].sort()

print(*dfs(tree, v))
print(*bfs(tree, v))
