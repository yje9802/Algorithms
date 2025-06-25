from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_dq = deque(truck_weights)
    
    curr_bridge = deque([0] * bridge_length)
    curr_weight = 0
    while curr_bridge:
        answer += 1
        curr_weight -= curr_bridge.popleft()
        
        if truck_dq:
            if curr_weight + truck_dq[0] <= weight:
                curr_bridge.append(truck_dq.popleft())
                curr_weight += curr_bridge[-1]
            else: # 다리에 트럭 더 못 올라감
                curr_bridge.append(0)
        
    return answer