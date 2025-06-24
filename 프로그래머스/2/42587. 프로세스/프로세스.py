from collections import deque

def solution(priorities, location):
    answer = 0
    
    process = deque([])
    for i in range(len(priorities)):
        process.append((priorities[i], i))
    priority_order = deque(sorted(priorities))

    top_priority = priority_order.pop()
    
    while process:
        head = process.popleft()
        if head[0] == top_priority:
            answer += 1
            if head[1] == location:
                break
            else:
                top_priority = priority_order.pop()
        else:
            process.append(head)
        
    return answer