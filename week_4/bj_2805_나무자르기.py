# 백준 2805번 - 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline


def solution(n, m, trees_len):
    answer = 0
    start = 0
    end = max(trees_len)

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for tree in trees_len:
            if tree > mid:
                total += tree - mid

            if total >= m:
                break

        if total >= m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer


n, m = map(int, input().split())
trees_len = list(map(int, input().split()))

print(solution(n, m, trees_len))
