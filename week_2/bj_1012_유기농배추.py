# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10_000)


def dfs(x, y):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)


# [[1, 0, 0, 0, 0, 0, 0, 0],
#  [1, 1, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 1, 1, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 1, 1, 1, 0]]
