from collections import defaultdict

def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def solution(info, query):
    answer = []
    
    db = defaultdict(list)
    
    for row in info:
        parts = row.split()
        conditions = parts[:4] # 개발언어, 직군, 경력, 소울푸드
        score = int(parts[4]) # 지원자 점수
        
        for mask in range(16):
            key_parts = []
            for i in range(4):
                if mask & (1 << i):
                    key_parts.append('-')
                else:
                    key_parts.append(conditions[i])
            key = ''.join(key_parts)
            db[key].append(score)
    
    for k in db:
        db[k].sort()
    
    for q in query:
        q = q.replace(" and ", " ")
        parts = q.split()
        key = ''.join(parts[:4])
        score_range = int(parts[4])
        
        scores = db[key]
        idx = lower_bound(scores, score_range)
        answer.append(len(scores) - idx)
    return answer