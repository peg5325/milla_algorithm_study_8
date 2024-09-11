# 백준 1654번 - 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys


def solution(k, n, k_list):
    answer = 0
    start = 1
    end = max(k_list)

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for length in k_list:
            count += length // mid

        if count >= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


k, n = map(int, sys.stdin.readline().split())
k_list = list(int(sys.stdin.readline()) for _ in range(k))

print(solution(k, n, k_list))
