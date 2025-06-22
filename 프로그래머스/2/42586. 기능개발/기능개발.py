from collections import deque

def solution(progresses, speeds):
    answer = []
    
    for_done = deque([]) # 진도 100% 되는 일수
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        for_done.append(left // speeds[i] if left % speeds[i] == 0 else left // speeds[i] + 1)
    
    cnt = 1
    start = for_done.popleft() # 먼저 배포되어야 하는 작업의 완료 시점
    while for_done:
        nxt = for_done.popleft()
        if nxt <= start:
            cnt += 1
        else:
            answer.append(cnt)
            start = nxt
            cnt = 1
    answer.append(cnt)
    return answer