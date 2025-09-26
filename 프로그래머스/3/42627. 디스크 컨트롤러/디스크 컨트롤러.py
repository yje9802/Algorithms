import heapq

def solution(jobs):
    answer = 0
    
    n = len(jobs)
    jobs.sort(key=lambda x: x[0]) # 요청 시간 기준으로 정렬
    
    heap = []
    time = 0
    i = 0
    
    while i < n or heap:
        # 현재까지 요청된 작업 heap에 넣기
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0])) # (소요시간, 요청시점)
            i += 1 # 인덱스 증가
        
        if heap: # 대기 큐가 비어있지 않음
            work_time, req_time = heapq.heappop(heap)
            time += work_time # 작업을 마친 시간
            answer += time - req_time # 반환 시간
        else: # 처리할 작업이 없다면 다음 작업 요청 시간으로 넘어감
            time = jobs[i][0]
    
    answer = answer // n
    return answer