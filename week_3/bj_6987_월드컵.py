# 백준 6987번 - 월드컵
# https://www.acmicpc.net/problem/6987

def is_valid(result, matches, index=0):
    if index == 15:  # 15개의 경기 결과를 모두 확인했으면
        return all(sum(result[i]) == 0 for i in range(6))

    t1, t2 = matches[index]
    for outcome in [(0, 2), (1, 1), (2, 0)]:  # (승, 패), (무, 무), (패, 승)
        if result[t1][outcome[0]] > 0 and result[t2][outcome[1]] > 0:
            result[t1][outcome[0]] -= 1
            result[t2][outcome[1]] -= 1

            if is_valid(result, matches, index + 1):
                return True

            result[t1][outcome[0]] += 1
            result[t2][outcome[1]] += 1

    return False

def solve():
    matches = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
               (1, 2), (1, 3), (1, 4), (1, 5),
               (2, 3), (2, 4), (2, 5),
               (3, 4), (3, 5),
               (4, 5)]

    results = []
    for _ in range(4):  # 4개의 테스트 케이스를 처리
        data = list(map(int, input().split()))
        result = [data[i*3:(i+1)*3] for i in range(6)]  # 6개 국가의 경기 결과를 리스트로 분할
        if is_valid(result, matches):
            results.append(1)
        else:
            results.append(0)

    print(" ".join(map(str, results)))

solve()
