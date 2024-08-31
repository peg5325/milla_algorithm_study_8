# 백준 2178번 - 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque


def bfs(maze, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    distance = [[0] * m for _ in range(n)]

    queue = deque([(0, 0)])
    distance[0][0] = 1  # 시작점의 거리 1로 설정

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                if distance[nx][ny] == 0:  # 아직 방문하지 않은 칸
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    # 도착점 (n-1, m-1)까지의 거리 반환
    return distance[n-1][m-1]


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

print(bfs(maze, n, m))
