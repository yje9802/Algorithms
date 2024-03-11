def solution(n):
    answer = []
    
    def hanoi(start, end, extra, n):
        if n == 1:
            answer.append([start, end])

        else:
            hanoi(start, extra, end, n-1)
            hanoi(start, end, extra, 1)
            hanoi(extra, end, start, n-1)
    
    hanoi(1, 3, 2, n) # 1번에서 출발, 3번 도착, 여분 기둥 2번, 원판 개수 n
    
    return answer