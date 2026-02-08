def convert_time(time_list): # 문자열"hour:minute"을 분 단위로 변환
    hour, minute = time_list.split(":")
    return int(hour) * 60 + int(minute)

def solution(book_time):
    answer = 0
    
    rooms = [0 for _ in range(24*60 + 10)]
    
    for booked in book_time:
        start = convert_time(booked[0])
        end = convert_time(booked[1]) + 10
        
        rooms[start] += 1
        rooms[end] -= 1
    
    # 누적합 구하기
    for i in range(1, len(rooms)):
        rooms[i] = rooms[i-1] + rooms[i]
    answer = max(rooms)
    return answer