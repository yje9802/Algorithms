def solution(bandage, health, attacks):
    answer = health
    
    i = 1 # 현재 시간
    skill = 0 # 기술 연속 성공; 최대 bandage[0]까지
    
    while len(attacks) > 0:
        if i == attacks[0][0]: # 공격 시점
            answer -= attacks[0][1]
            skill = 0 # 연속 성공 초기화
            attacks.pop(0)
            if answer <= 0: # 체력이 0 이하가 되면 종료
                answer = -1
                break
        else:
            answer += bandage[1]
            if answer >= health: # 최대 체력보다 많이 회복할 수 없다.
                answer = health
            skill += 1
            if skill == bandage[0]: # t초 연속으로 기술 성공 -> 체력 추가 회복
                answer += bandage[2]
                if answer >= health:
                    answer = health
                skill = 0
        i += 1
        
    return answer