def solution(picks, minerals):
    answer = 0
    
    n = sum(picks) # 곡괭이 개수
    k = n*5 if n * 5 < len(minerals) else len(minerals) # 곡괭이로 캘 수 있는 양
    
    hards = []
    for i in range(0, k, 5):
        chunk = minerals[i:i+5] # 광물 5개씩
        d = chunk.count("diamond")
        ir = chunk.count("iron")
        s = chunk.count("stone")
        hard = d * 25 + ir * 5 + s
        hards.append((hard, d, ir, s))
    
    # 피로도가 높은 순으로 내림차순 정렬
    hards.sort(reverse=True, key=lambda x: x[0])
    
    for hard, d, ir, s in hards:
        if picks[0] > 0: # 다이아 곡괭이가 남아 있다면
            picks[0] -= 1
            answer += d + ir + s
        elif picks[1] > 0:
            picks[1] -= 1
            answer += 5 * d + ir + s
        elif picks[2] > 0:
            picks[2] -= 1
            answer += hard
        else:
            break
    
    return answer