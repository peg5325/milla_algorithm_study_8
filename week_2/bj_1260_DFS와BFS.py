# 백준 1260번 - DFS 와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque, defaultdict

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def main():
    n, m, v = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 방문 리스트를 노드의 개수만큼 False로 초기화
    visited = [False] * (n + 1)

    dfs(graph, v, visited)
    print()

    # BFS를 위해 visited 리스트 초기화
    visited = [False] * (n + 1)

    bfs(graph, v, visited)

if __name__ == "__main__":
    main()