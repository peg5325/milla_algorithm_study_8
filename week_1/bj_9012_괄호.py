# 백준 9012번 - 괄호
# https://www.acmicpc.net/problem/9012

from sys import stdin


input = stdin.readline

# --- 나의 풀이 ---

t = int(input())

for _ in range(t):
    string = input().strip()
    open = 0
    close = 0

    for i in range(len(string)):
        if '(' == string[i]:
            open += 1
        elif ')' == string[i]:
            close += 1

        if open < close:    # 닫히는 괄호의 갯수가 여는 괄호의 갯수보다 많아지는 순간 VPS가 아니게 됨.
            break

    if open == close:
        print("YES")
    else:
        print("NO")


# --- 스택을 활용한 문제 풀이 ---
# 참조 : https://omins.tistory.com/34

# t = int(input())
#
# for _ in range(t):
#     stack = []
#     string = input()
#     isVPS = True
#
#     for check in string:
#         if check == '(':
#             stack.append('(')
#         if check == ')':
#             if stack:
#                 stack.pop()
#             elif not stack:
#                 isVPS = False
#                 break
#     if not stack and isVPS:
#         print('YES')
#     elif stack or not isVPS:
#         print('NO')
