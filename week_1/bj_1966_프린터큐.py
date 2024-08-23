# 백준 1966번 - 프린터 큐
# https://www.acmicpc.net/problem/1966

from sys import stdin
from collections import deque


def soultion(n, m, print_list):
    count = 0
    target = print_list[m]
    order_arr = deque(i for i in range(len(print_list)))

    while print_list:
        import_num = max(print_list)

        if import_num == print_list[0]:
            count += 1
            if target == print_list[0] and m == order_arr[0]:
                break
            else:
                print_list.popleft()
                order_arr.popleft()
        else:
            print_list.rotate(-1)
            order_arr.rotate(-1)

    return count


input = stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print_list = deque(map(int, input().split()))
    print(soultion(n, m, print_list))

# --- 주어진 예시 ---

# print(soultion(1, 0, deque([5])))
# print(soultion(4, 2, deque([1, 2, 3, 4])))
# print(soultion(6, 0, deque([1, 1, 9, 1, 1, 1])))


