# from sys import stdin
#
#
# input = stdin.readline
#
# n, k = map(int, input().split())
#
# arr = [i for i in range(1, n+1)]
# result_arr = []
# count = 1
# index = 0
#
# while len(arr) != 0:
#     if len(arr) == 1:
#         result_arr.append(arr[0])
#         break
#
#     if count == 3:
#         result_arr.append(arr[index])
#         del arr[index]
#         index -= 1
#         count = 0
#
#     if index == len(arr) - 1:
#         index = 0
#         count += 1
#     else:
#         index += 1
#         count += 1
#
# print("<", end="")
# print(*result_arr, sep=', ', end="")
# print(">")


# --- 정답 ---

n, k = map(int, input().split())
ans = []
arr = [i for i in range(1, n+1)]
num = 0
for i in range(n):
    num += (k-1)
    if num >= len(arr):
        num %= len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)

print("<", ", ".join(ans), ">", sep="")