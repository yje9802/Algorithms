from collections import deque

def solution(plans):
    answer = []
    
    # 문자열로 저장된 시간을 int형으로 변환하는 작업
    for plan in plans:
        times = list(map(int, plan[1].split(":"))) # [hour, min]
        plan[1] = times[0]*60 + times[1] # "11:40" -> 700 이렇게 분 단위로 변환
        plan[2] = int(plan[2])
    
    plans.sort(key=lambda x: x[1]) # plans를 과제 시작 시간 기준으로 정렬
    
    hws = deque() # [name, playtime]
    
    for i in range(len(plans)-1):
        name, start, playtime = plans[i]
        hws.append([name, playtime])
        
        time_gap = plans[i+1][1] - start # 다음 과제 시작 전까지 남은 시간
        
        while hws and time_gap > 0:
            q_name, q_lefttime = hws.pop()
            if q_lefttime <= time_gap:
                time_gap -= q_lefttime
                answer.append(q_name)
            else:
                hws.append([q_name, q_lefttime - time_gap])
                time_gap = 0 # 리셋 and 루프 중단
    
    answer.append(plans[-1][0]) # 마지막에 시작하는 과제는 굳이 hws에 들어갈 필요는 없다.
    while hws:
        name, _ = hws.pop()
        answer.append(name)
        
    return answer