import heapq

def solution(n, k, enemy):
    answer = 0
    
    hq = []
    for en in enemy:
        if n >= en: # 무적권 없이 적군 처리 가능
            n -= en
            heapq.heappush(hq, -en)
        else:
            if k == 0: # 쓸 수 없는 무적권도 없음
                break
            else:
                n -= en
                k -= 1 # 무적권 하나 소모
                heapq.heappush(hq, -en)
                credit = -heapq.heappop(hq)
                n += credit # 무적권 사용으로 병사 수 복구
        answer += 1
    return answer