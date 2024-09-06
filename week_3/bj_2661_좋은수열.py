# 백준 2661번 - 좋은수열
# https://www.acmicpc.net/problem/2661

import sys
sys.setrecursionlimit(10_000)


# def check(num):
#     for i in range(1, (len(num) // 2) + 1):
#         if num[-i:] == num[-(i * 2):-i]:
#             return False
#     else:
#         return True
#
#
# def solution(num):
#     global n
#
#     if len(num) == n:
#         print(num)
#         return
#
#     for i in range(1, 4):
#         num.append(i)
#         if check(num):
#             solution(num)
#         else:
#             num.pop()
#
#
# n = int(sys.stdin.readline())
# num = [1]
#
# solution(num)

# -- 하위 정답 코드 --

def check(num):
    for i in range(1, (len(num) // 2) + 1):
        if num[-i:] == num[-(i * 2):-i]:
            return False
    return True


def solution(num):
    global n

    if len(num) == n:
        print("".join(map(str, num)))
        sys.exit()  # 정답을 찾으면 프로그램을 종료

    for i in range(1, 4):
        num.append(i)
        if check(num):
            solution(num)
        num.pop()  # 무조건 pop() 호출해서 숫자를 제거


n = int(input())
num = [1]

solution(num)
