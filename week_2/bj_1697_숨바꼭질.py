# 백준 1697번 - 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(N, K):
    # 방문한 위치를 기록하는 리스트, 최대 100,000까지 가능
    visited = [False] * 100_001

    # BFS를 위한 큐 초기화
    queue = deque([(N, 0)])  # (현재 위치, 시간)
    visited[N] = True

    while queue:
        current_position, current_time = queue.popleft()

        # 동생의 위치에 도달하면 현재 시간을 반환
        if current_position == K:
            return current_time

        # 다음 가능한 이동 위치 계산
        next_positions = [current_position - 1, current_position + 1, current_position * 2]
        for next_position in next_positions:
            if 0 <= next_position <= 100_000 and not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, current_time + 1))

# 입력 처리
N, K = map(int, input().split())
# 결과 출력
print(bfs(N, K))
