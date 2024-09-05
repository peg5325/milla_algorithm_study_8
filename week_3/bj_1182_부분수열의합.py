# 백준 1182번 - 부분 수열의 합
# https://www.acmicpc.net/problem/1182

import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, n+1):
    combi = combinations(nums, i)

    for x in combi:
        if sum(x) == s:
            count += 1

print(count)
