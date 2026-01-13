def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    curr = -1 # 가장 최근에 요격 미사일 발사 지점

    for target in targets:
        s, e = target
        if curr <= s:
            answer += 1
            curr = e
    
    return answer