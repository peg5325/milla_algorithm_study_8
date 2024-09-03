# 백준 15663번 - N과 M(9)
# https://www.acmicpc.net/problem/15663

import sys

def solution(N, M, nums, start = 0, seq = []):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return

    nums = sorted(set(nums))

    for i in range(start, len(nums)):
        seq.append(nums[i])
        solution(N, M, nums, i, seq)
        seq.pop()


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

solution(N, M, nums)
