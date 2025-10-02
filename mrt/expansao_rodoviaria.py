import sys
from collections import deque

def solve():
    # Ler linha por linha ao invés de sys.stdin.read()
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # BFS para tentar reconstruir árvore
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

    # árvore precisa ter N-1 arestas
    if len(edges) != n-1:
        print("*")
        return

    tree_set = set((min(a,b), max(a,b)) for a,b in edges)

    # Contar quantas arestas extras existem (não estão na árvore)
    extra_edges = 0
    for u in range(1, n+1):
        for v in graph[u]:
            if u < v:
                if (u,v) not in tree_set:
                    extra_edges += 1
                    # precisa ter mesmo pai (distância 2 na árvore)
                    if parent[u] != parent[v]:
                        print("*")
                        return

    # Se não há arestas extras, não houve expansão - inválido
    if extra_edges == 0:
        print("*")
        return

    # Se válido, imprime as N-1 arestas
    for u,v in edges:
        print(u, v)

if __name__ == "__main__":
    solve()
