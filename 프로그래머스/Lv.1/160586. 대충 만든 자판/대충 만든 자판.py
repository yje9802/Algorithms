def get_cnt(s, keymap):
    location = 150
    for key in keymap:
        if s in key:
            location = min(location, key.find(s)+1)
    return location

def solution(keymap, targets):
    answer = [0 for _ in range(len(targets))]
    dict = {}
    
    for i in range(len(targets)):
        for t in targets[i]:
            if t in dict:
                answer[i] += dict[t]
            else:
                loc = get_cnt(t, keymap)
                if loc == 150:
                    answer[i] = -1
                    break
                dict[t] = loc
                answer[i] += loc

    
    return answer