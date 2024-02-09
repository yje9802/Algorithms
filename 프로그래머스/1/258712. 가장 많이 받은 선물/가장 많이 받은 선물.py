def solution(friends, gifts):
    gifted = {} # gifted = {"friend 이름": {"선물 준 친구 이름": 이 친구에게 준 선물 개수}}
    gift_idx = {} # 선물 지수 
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0
    
    for gift in gifts:
        t, f = gift.split(' ') # t: 선물을 준 사람 f: 받은 사람
        if f in gifted[t]:
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1
        # 선물 지수 계산
        gift_idx[t] += 1
        gift_idx[f] -= 1
        
    will_get = [0 for _ in friends] # 각자 받게될 선물 개수
    for i in range(len(friends)):
        curr = friends[i]
        for j in range(i+1, len(friends)):
            another = friends[j]
            a = gifted[curr][another] if another in gifted[curr] else 0
            b = gifted[another][curr] if curr in gifted[another] else 0
            if a > b: 
                will_get[i] += 1
            elif a < b:
                will_get[j] += 1
            elif a == b:
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1
    
    answer = max(will_get)
    return answer