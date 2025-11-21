import math
from collections import defaultdict, deque

def hour_to_min(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    answer = []
    
    minimum, min_fee, extra, extra_fee = fees
    car_dict = defaultdict(list)
    
    for record in records:
        rec_split = record.split(" ")
        minutes = hour_to_min(rec_split[0])
        car_dict[rec_split[1]].append(minutes)
    
    maximum_hour = 23 * 60 + 59
    for k in sorted(car_dict.keys()):
        v = deque(car_dict[k])
        total_fee = min_fee # 현재까지의 요금
        
        total_time = 0
        while v:
            if len(v) == 1:
                curr = v.popleft()
                total_time += maximum_hour - curr
            else:
                curr, nxt = v.popleft(), v.popleft()
                total_time += abs(nxt - curr)
        
        if total_time - minimum > 0:
            total_fee += math.ceil((total_time - minimum) / extra) * extra_fee
        answer.append(total_fee)
    return answer