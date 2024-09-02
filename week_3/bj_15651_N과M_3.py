# 백준 15651번 - N과 M(3)
# https://www.acmicpc.net/problem/15651

import sys


def backtrack(N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        sequence.append(i)
        backtrack(N, M, sequence)
        sequence.pop()


def solve(N, M):
    backtrack(N, M, [])


# 입력 예시
N, M = map(int, sys.stdin.readline().split())
solve(N, M)
