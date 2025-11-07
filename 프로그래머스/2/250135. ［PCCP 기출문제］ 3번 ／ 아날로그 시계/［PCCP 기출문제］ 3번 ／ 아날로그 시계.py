def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 시작하는 지점과 끝나는 지점을 초로 환산
    start = h1 * 60**2 + m1 * 60 + s1
    end = h2 * 60**2 + m2 * 60 + s2
    
    # 시작하는 지점이 0시 0분 0초이거나 12시 0분 0초인 경우
    if start == 0 or start == 12 * 60**2:
        answer += 1
    
    # 1초 단위로 루프 돌기
    while start < end:
        # 현재의 시침, 분침, 초침 위치
        h = start * (1/120) % 360
        m = start * (1/10) % 360
        s = start * 6 % 360
        
        # 다음 초에서 시침, 분침, 초침의 각도 계산
        # 0이 나오면 정각으로 돌아갔다는 의미라, 360으로 놓고 계산
        hh = 360 if (start+1) * (1/120) % 360 == 0 else (start+1) * (1/120) % 360
        mm = 360 if (start+1) * (1/10) % 360 == 0 else (start+1) * (1/10) % 360
        ss = 360 if (start+1) * 6 % 360 == 0 else (start+1) * 6 % 360
        
        if s < h and ss >= hh:
            answer += 1
        if s < m and ss >= mm:
            answer += 1
        # 시침, 분침, 초침이 모두 겹치면 1번만 알람 울린 것으로 처리
        if ss == hh and ss == mm:
            answer -= 1
        
        # 다음 초로 넘어가기
        start += 1
        
    return answer