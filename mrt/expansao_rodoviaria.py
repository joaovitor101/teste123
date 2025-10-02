import sys
from collections import deque

def solve():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    root = 1
    parent = [-1]*(n+1)
    visited = [False]*(n+1)

    q = deque([root])
    visited[root] = True
    edges = []

    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                edges.append((u, v))
                q.append(v)

    if len(edges) != n-1:
        print("*")
        return

    tree_set = set((min(a,b), max(a,b)) for a,b in edges)

    extra_edges = 0
    for u in range(1, n+1):
        for v in graph[u]:
            if u < v:
                if (u,v) not in tree_set:
                    extra_edges += 1
                    if parent[u] != parent[v]:
                        print("*")
                        return

    if extra_edges == 0:
        print("*")
        return

    for u,v in edges:
        print(u, v)

if __name__ == "__main__":
    solve()
