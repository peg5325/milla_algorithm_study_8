# 프로그래머스 > 이분탐색 > 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3

def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total_people = 0

        for time in times:
            total_people += mid // time

            if total_people >= n:
                break

        if total_people >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer


# 예제 조건
# input : n = 6, times = [7, 10]
# output : 28

print(solution(6, [7, 10]))
