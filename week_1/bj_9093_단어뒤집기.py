# 백준 9093번 - 단어 뒤집기
# https://www.acmicpc.net/problem/9093

from sys import stdin

input = stdin.readline
t = int(input())

for _ in range(t):
    sentance = input().split()

    for i in range(0, len(sentance)):
        word = sentance[i]
        sentance[i] = word[::-1]

    print(" ".join(sentance))