def solution(mats, park):
    answer = -1
    
    mats.sort(reverse=True) # 깔 수 있는 가장 큰 돗자리를 찾음
    
    opt_park = []
    for p in park:
        opt_p = []
        for l in p:
            if l != "-1": opt_p.append(0)
            else: opt_p.append(1)
        opt_park.append(opt_p)
    
    for m in mats:
        i = 0
        space = 0
        while i <= len(park)-m:
            for j in range(0, len(park[0])-m+2):
                if sum(opt_park[i][j:j+m]) == m:
                    for k in range(i, i+m):
                        temp = sum(opt_park[k][j:j+m])
                        if temp != m:
                            space = 0
                            break
                        space += temp
                    if space == m*m: return m
                else:
                    space = 0
            i += 1
    
    return answer