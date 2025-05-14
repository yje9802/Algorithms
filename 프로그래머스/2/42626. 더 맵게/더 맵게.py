import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0 and first < K:
            answer = -1
            break
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        heapq.heappush(scoville, mixed)
        answer += 1
    
    return answer