# 백준 1495번 - 기타리스트
# https://www.acmicpc.net/problem/1495

import sys
input = sys.stdin.readline


def guitar_playlist(N, S, M, volumes):
    # DP 테이블을 선언 (N+1 x M+1) 곡과 볼륨 정보를 저장하는 2차원 배열
    dp = [[False] * (M + 1) for _ in range(N + 1)]

    # 첫 번째 곡의 시작 볼륨 S 설정
    dp[0][S] = True

    # 각 곡에 대해 DP 테이블 갱신
    for i in range(1, N + 1):
        for v in range(M + 1):
            if dp[i - 1][v]:
                # 볼륨을 높일 수 있는 경우
                if v + volumes[i - 1] <= M:
                    dp[i][v + volumes[i - 1]] = True
                # 볼륨을 낮출 수 있는 경우
                if v - volumes[i - 1] >= 0:
                    dp[i][v - volumes[i - 1]] = True

    # 마지막 곡에서 가능한 최대 볼륨을 찾기
    for v in range(M, -1, -1):
        if dp[N][v]:
            return v

    # 마지막 곡에서 가능한 볼륨이 없다면 -1 출력
    return -1


# 입력 예시
N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

# 결과 출력
print(guitar_playlist(N, S, M, volumes))
