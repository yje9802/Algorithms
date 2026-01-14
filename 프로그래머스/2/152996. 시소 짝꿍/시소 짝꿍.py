from collections import defaultdict

def solution(weights):
    answer = 0
    
    weights.sort()
    cnt = defaultdict(int)
    
    for w in weights:
        # 1:1
        answer += cnt[w]

        # 2:3
        if w % 3 == 0:
            answer += cnt[w * 2 // 3]

        # 1:2
        if w % 2 == 0:
            answer += cnt[w // 2]

        # 3:4
        if w % 4 == 0:
            answer += cnt[w * 3 // 4]

        cnt[w] += 1
    return answer