# 백준 1759번 - 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations


def solution(combi):

    for x in combi:
        consonant_cnt = 0
        vowel_cnt = 0

        for i in x:
            if i in "aeiou":
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if consonant_cnt >= 2 and vowel_cnt >= 1:
            print("".join(x))


l, c = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))

sorted_alpha = sorted(alphabets)

# 틀린 부분
combi = combinations(sorted_alpha, 4)

solution(combi)
