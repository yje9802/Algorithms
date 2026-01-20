import heapq

def convert_time(time_list):
    hour, minute = time_list.split(":")
    return int(hour) * 60 + int(minute)

def solution(book_time):
    answer = 0
    
    times = []
    for time in book_time:
        start, end = time
        heapq.heappush(times, [convert_time(start), convert_time(end) + 10])
    
    temp = []
    
    # 첫번째 방은 무조건 필요
    _, end = heapq.heappop(times)
    heapq.heappush(temp, end)
    answer += 1
    
    while times:
        start, end = heapq.heappop(times)
        earlist = heapq.heappop(temp)
        heapq.heappush(temp, end)
        if earlist > start:
            heapq.heappush(temp, earlist)
            answer += 1
        
    return answer