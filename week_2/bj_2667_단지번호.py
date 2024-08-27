# 백준 2667번 - 단지번호 붙이기
# https://www.acmicpc.net/problem/2667

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    # 현재 위치를 방문 처리
    visited[x][y] = True
    count = 1  # 현재 위치에서 시작하여 집 하나를 셈

    # 상하좌우로 이동하기 위한 좌표 변화
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도를 벗어나지 않고, 아직 방문하지 않았으며, 집이 있는 경우에만 재귀적으로 탐색
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '1':
            count += dfs(nx, ny)

    return count

# 입력 처리
n = int(input())
grid = [input().strip() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        # 집이 있고, 방문하지 않은 경우에만 DFS 시작
        if grid[i][j] == '1' and not visited[i][j]:
            result.append(dfs(i, j))

# 단지 수 출력
print(len(result))
# 각 단지의 집의 수를 오름차순으로 정렬하여 출력
result.sort()
for num in result:
    print(num)