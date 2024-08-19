from sys import stdin

input = stdin.readline

n = int(input())
arr = []


for i in range(n):
    command = input().strip()

    if "push" in command:
        arr.append(int(command[5:]))
    elif "top" == command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif "pop" == command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif "size" == command:
        print(len(arr))
    elif "empty" == command:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
