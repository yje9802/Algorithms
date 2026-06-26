from collections import deque

def solution(order):
    answer = 0
    
    sub = deque([])
    current = 1 # 마지막으로 꺼낸 상자
    n = len(order) # 전체 상자의 개수
    
    for box in order:
        while current <= n and current < box:
            sub.append(current)
            current += 1
        if current == box:
            answer += 1
            current += 1
        elif sub and box == sub[-1]:
            answer += 1
            sub.pop()
        else:
            break
            
    return answer