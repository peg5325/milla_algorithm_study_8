from collections import deque


def solution(bridge_length, weight, truck_weights):
    cnt = 0
    second = 0
    current_weight = 0
    bridge = deque([0] * bridge_length)

    while bridge:
        current_weight -= bridge.popleft()
        second += 1

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)

    return second


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


# --- 나의 답안 --- : 오답

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = []
#
#     while truck_weights:
#         answer += 1
#
#         if len(bridge) == bridge_length:
#             bridge.pop(0)
#
#         if sum(bridge) == 0:
#             bridge.append(truck_weights[0])
#             truck_weights.pop(0)
#         elif sum(bridge) < weight:
#             if sum(bridge) + truck_weights[0] <= weight and len(bridge) < bridge_length:
#                 bridge.append(truck_weights[0])
#                 truck_weights.pop(0)
#             else:
#                 bridge.append(0)
#
#     answer += bridge_length
#     return answer

# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
