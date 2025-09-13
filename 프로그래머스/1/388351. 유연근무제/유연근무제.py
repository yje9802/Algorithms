def cal_limit(schedule):
    plused = schedule % 100 + 10
    new_hour = schedule // 100 + (plused // 60)
    new_min = plused % 60
    return new_hour * 100 + new_min

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        today = startday # 시작 요일
        limit = cal_limit(schedules[i])
        cnt = 0
        for timelog in timelogs[i]:
            if today >= 6:
                today = 1 if today == 7 else today + 1
                continue
            if timelog <= limit:
                cnt += 1
            else:
                break
            today += 1
        if cnt == 5:
            answer += 1
        
    return answer