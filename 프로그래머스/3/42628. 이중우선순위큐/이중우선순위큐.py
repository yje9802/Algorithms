import heapq

def solution(operations):
    answer = []
    
    min_h = [] # 최소힙
    max_h = [] # 최대힙
    visited = [False] * len(operations) # 지워진 값은 False

    for i, op in enumerate(operations):
        if op.startswith('I'):
            num = int(op[2:])
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True
        else:
            if op == "D 1":
                while max_h and not visited[max_h[0][1]]: # 이미 지워진 값 삭제
                    heapq.heappop(max_h)
                if max_h: # 아직 큐에 값이 남아있다면
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            elif op == "D -1":
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)
    
    # 양쪽 힙에서 이미 지워진 값 제거
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    
    if not min_h or not max_h:
        answer = [0, 0]
    else:
        answer = [-max_h[0][0], min_h[0][0]]
    
    return answer