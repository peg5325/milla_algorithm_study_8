# 백준 12026번 - BOJ 거리
# https://www.acmicpc.net/problem/12026

import sys
input = sys.stdin.readline


def solution():
    # 입력처리
    n = int(input())
    blocks = input().strip()

    # DP 배열 생성
    dp = [float('inf')] * n

    # 출발 지점은 에너지 불필요
    dp[0] = 0

    # 필요한 에너지 계산
    # 조건에 맞게 B -> O -> J -> B 순서가 맞는지 체크
    for i in range(n):
        for j in range(i + 1, n):
            if (blocks[i] == 'B' and blocks[j] == 'O') or (blocks[i] == 'O' and blocks[j] == 'J') or (blocks[i] == 'J' and blocks[j] == 'B'):
                dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

    if dp[n - 1] == float('inf'):
        print(-1)
    else:
        print(dp[n - 1])


solution()
