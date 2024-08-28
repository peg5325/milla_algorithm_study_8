# 백준 11724번 - 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connected_components = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        connected_components += 1

print(connected_components)
